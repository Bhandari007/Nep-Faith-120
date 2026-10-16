"""NepFaith-120: Canonical Data Schema v1

Frozen specification for all corpus items, claims, and annotation records.
Every field is explicitly tied to a downstream analysis or pipeline consumer.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class Domain(str, Enum):
    WIKIPEDIA = "wikipedia"
    GOVERNMENT_REPORT = "government_report"
    NEWS = "news"


class Provenance(str, Enum):
    NATURAL = "natural"
    PERTURBED = "perturbed"


class PerturbationType(str, Enum):
    ENTITY_SWAP = "entity_swap"
    NUMBER_DATE_ALTERATION = "number_date_alteration"
    NEGATION_FLIP = "negation_flip"
    MISATTRIBUTION = "misattribution"
    REGISTER_SHIFT = "register_shift"
    UNSUPPORTED_ADDITION = "unsupported_addition"
    INVENTED_CAUSALITY = "invented_causality"


class RetrievalCondition(str, Enum):
    FULL_SUPPORT = "full_support"
    PARTIAL_SUPPORT = "partial_support"
    DISTRACTOR_PRESENT = "distractor_present"


class ClaimLabel(str, Enum):
    SUPPORTED = "Supported"
    CONTRADICTED = "Contradicted"
    NOT_IN_CONTEXT = "Not-in-context"


class AtomicClaim(BaseModel):
    """Atomic factual proposition extracted from the generated answer."""
    claim_id: str = Field(description="Unique claim identifier, formatted as {item_id}_c{idx}")
    claim_text: str = Field(description="Self-contained atomic proposition in English")
    is_critical: bool = Field(default=True, description="Critical to user query; triggers item-level failure if ungrounded")
    gold_label: Optional[ClaimLabel] = Field(default=None, description="Human consensus ground truth label")
    
    # Model proxy predictions across experimental conditions
    c1_pred: Optional[ClaimLabel] = Field(default=None, description="Prediction under Condition C1 (Cross-lingual Nepali context)")
    c2_pred: Optional[ClaimLabel] = Field(default=None, description="Prediction under Condition C2 (Raw MT English context)")
    c3_pred: Optional[ClaimLabel] = Field(default=None, description="Prediction under Condition C3 (Post-edited MT English context)")


class EvaluationItem(BaseModel):
    """Core evaluation record representing a single paired item."""
    item_id: str = Field(description="Unique item identifier, formatted as {domain}_{idx}")
    domain: Domain = Field(description="Corpus source domain for stratified variance estimation")
    sub_genre: Optional[str] = Field(default=None, description="Sub-genre descriptor, e.g. 'health', 'agriculture', 'sports'")
    source_provenance: Provenance = Field(description="Natural RAG generation vs. perturbed counterfactual")
    source_url: Optional[str] = Field(default=None, description="Traceable live URL or published report identifier")
    source_title: Optional[str] = Field(default=None, description="Published article or report title")
    perturbation_type: Optional[PerturbationType] = Field(
        default=None, description="Typed edit category for hypothesis H2 testing; null for natural items"
    )
    perturbation_span: Optional[str] = Field(default=None, description="Target text span altered by perturbation")
    
    # Text contexts
    passage_ne: str = Field(description="Original Nepali reference passage (Condition C1)")
    query_ne: Optional[str] = Field(default=None, description="Original Nepali query if applicable")
    query_en: str = Field(description="English query submitted to the RAG system")
    answer_en: str = Field(description="Generated English response subject to faithfulness verification")
    
    # Counterfactual passages
    c2_raw_mt: Optional[str] = Field(default=None, description="IndicTrans2 raw machine translation of passage_ne")
    c3_post_edited_mt: Optional[str] = Field(default=None, description="Human post-edited translation of c2_raw_mt")
    
    # Sampling & Stratification
    retrieval_condition: RetrievalCondition = Field(description="Stratification factor: full, partial, or distractor support")
    sampling_weight: float = Field(default=1.0, ge=0.0, description="Inverse probability sampling stratum weight")
    
    # Claims & Judgments
    claims: List[AtomicClaim] = Field(min_length=1, description="List of segmented atomic factual claims")
    derived_item_label: Optional[bool] = Field(
        default=None, description="Overall faithfulness verdict: True iff all claims Supported and no critical failure"
    )

    @field_validator("perturbation_type")
    @classmethod
    def validate_perturbation(cls, v, info):
        provenance = info.data.get("source_provenance")
        if provenance == Provenance.PERTURBED and v is None:
            raise ValueError("Perturbed items must specify a valid perturbation_type")
        if provenance == Provenance.NATURAL and v is not None:
            raise ValueError("Natural items cannot have a perturbation_type")
        return v

    def compute_derived_label(self) -> Optional[bool]:
        """Calculates item-level faithfulness with critical claim override."""
        if not self.claims or any(c.gold_label is None for c in self.claims):
            return None
        
        for c in self.claims:
            if c.is_critical and c.gold_label in (ClaimLabel.CONTRADICTED, ClaimLabel.NOT_IN_CONTEXT):
                return False
            if c.gold_label != ClaimLabel.SUPPORTED:
                return False
        return True


class CorpusPassage(BaseModel):
    """Raw or preprocessed reference passage before answer generation."""
    passage_id: str = Field(description="Unique passage identifier, e.g. wiki_001, gov_014, sports_003")
    domain: Domain = Field(description="Corpus domain: wikipedia | government_report | news")
    sub_genre: Optional[str] = Field(default=None, description="Sub-genre descriptor, e.g. 'sports', 'macroeconomics', 'census'")
    source_title: str = Field(description="Title of document, article, or gazette")
    source_url: Optional[str] = Field(default=None, description="Original source URL or formal citation")
    license: str = Field(description="License tag, e.g. CC-BY-SA-4.0, Nepal-Gov-Public-Domain, Academic-Fair-Dealing")
    passage_ne: str = Field(description="Normalized Nepali passage text in Devanagari script")
    token_count: int = Field(description="Word/token count of passage_ne")
    publication_year: Optional[int] = Field(default=None, description="Year of publication or report release")

