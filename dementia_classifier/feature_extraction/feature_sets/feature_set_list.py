import itertools


def cfg_features():
    return [
        "ADVP_to_RB",
        "INTJ_to_UH",
        "NP_to_DT_NN",
        "NP_to_PRP",
        "ROOT_to_FRAG",
        "VP_to_AUX",
        "VP_to_AUX_ADJP",
        "VP_to_AUX_VP",
        "VP_to_VBD_NP",
        "VP_to_VBG",
        "VP_to_VBG_PP",
        "CONJP",
        "UCP",
        "VP",
        "AvgNPTypeLengthEmbedded",
        "AvgNPTypeLengthNonEmbedded",
        "AvgPPTypeLengthEmbedded",
        "AvgPPTypeLengthNonEmbedded",
        "AvgVPTypeLengthEmbedded",
        "AvgVPTypeLengthNonEmbedded",
        "WHADJP",
        "WHAVP",
        "WHNP",
        "WHPP",
        "X",
        "FRAG",
        "INTJ",
        "LST",
        "NPTypeRate",
        "VPTypeRate",
        "PPTypeRate",
        "PProportion",
        "NPProportion",
        "VPProportion",
        "NAC",
        "NP",
        "NX",
        "PP",
        "PRN",
        "PRT",
        "QP",
        "RRC",
        "ADJP",
        "ADVP",
    ]


def syntactic_complexity_features():
    return[
        "MeanWordLength",
        "MLC",
        "MLS",
        "MLT",
        "DisfluencyFrequency",
        "TotalNumberOfWords",
        "number_of_utterances",
        "tree_height",
        "CN_C",
        "CN_T",
        "CP_C",
        "CP_T",
        "CT_T",
        "C_S",
        "C_T",
        "DC_C",
        "DC_T",
        "T_S",
        "VP_T",
        "C",
        "CN",
        "CP",
        "DC",
        "S",
        "T",
        "W",
        "CT"
    ]


def psycholinguistic_features():
    return[
        "getAoaScore",
        "getConcretenessScore",
        "getFamiliarityScore",
        "getImagabilityScore",
        "getSUBTLWordScores",
    ]


def vocabulary_richness_features():
    return [
        "MATTR",
        "BrunetIndex",
        "HonoreStatistic",
        "TTR",
    ]


def repetitiveness_features():
    return [
        "min_cos_dist",
        "proportion_below_threshold_0",
        "proportion_below_threshold_0.3",
        "proportion_below_threshold_0.5",
        "avg_cos_dist"
    ]


def acoustics_features():
    return [
        "mfcc13_mean",
        "mfcc1_mean",
        "mfcc7_vel_var",
        "mfcc1_vel_mean",
        "mfcc2_accel_skewness",
        "mfcc4_accel_skewness",
        "mfcc4_vel_kurtosis",
        "mfcc6_vel_skewness",
        "mfcc11_vel_skewness",
        "mfcc4_kurtosis",
        "mfcc8_vel_kurtosis",
        "mfcc7_vel_kurtosis",
        "mfcc3_vel_var",
        "mfcc3_accel_kurtosis",
        "mfcc8_skewness",
        "mfcc4_var",
        "mfcc8_accel_kurtosis",
        "mfcc10_kurtosis",
        "mfcc4_accel_kurtosis",
        "mfcc5_accel_skewness",
        "mfcc9_var",
        "mfcc3_accel_var",
        "mfcc7_vel_mean",
        "mfcc12_vel_var",
        "mfcc8_kurtosis",
        "mfcc7_mean",
        "mfcc7_accel_mean",
        "mfcc2_accel_mean",
        "mfcc1_accel_skewness",
        "mfcc2_var",
        "mfcc5_kurtosis",
        "mfcc11_accel_var",
        "mfcc12_skewness",
        "mfcc9_mean",
        "mfcc12_vel_mean",
        "mfcc2_vel_skewness",
        "mfcc12_kurtosis",
        "mfcc4_vel_skewness",
        "mfcc10_skewness",
        "mfcc4_vel_var",
        "mfcc12_mean",
        "mfcc6_vel_mean",
        "mfcc10_vel_kurtosis",
        "mfcc1_accel_mean",
        "mfcc1_kurtosis",
        "mfcc7_var",
        "mfcc10_mean",
        "mfcc7_kurtosis",
        "mfcc5_vel_mean",
        "mfcc2_mean",
        "mfcc7_accel_kurtosis",
        "mfcc2_accel_kurtosis",
        "mfcc6_vel_kurtosis",
        "mfcc1_vel_kurtosis",
        "mfcc11_skewness",
        "mfcc6_mean",
        "mfcc8_vel_var",
        "mfcc3_skewness",
        "mfcc5_skewness",
        "mfcc2_accel_var",
        "mfcc6_accel_skewness",
        "mfcc5_accel_mean",
        "mfcc1_vel_var",
        "mfcc6_vel_var",
        "mfcc10_accel_kurtosis",
        "mfcc8_var",
        "mfcc11_vel_kurtosis",
        "mfcc10_vel_mean",
        "mfcc1_skewness",
        "mfcc1_accel_var",
        "mfcc7_vel_skewness",
        "mfcc9_vel_mean",
        "mfcc2_vel_mean",
        "mfcc7_accel_var",
        "mfcc13_vel_var",
        "mfcc3_mean",
        "mfcc1_var",
        "mfcc_skewness",
        "mfcc5_accel_kurtosis",
        "mfcc1_vel_skewness",
        "mfcc5_accel_var",
        "mfcc12_vel_kurtosis",
        "mfcc6_accel_kurtosis",
        "mfcc5_mean",
        "mfcc12_accel_kurtosis",
        "mfcc4_mean",
        "mfcc11_kurtosis",
        "mfcc6_skewness",
        "mfcc2_vel_var",
        "mfcc9_skewness",
        "mfcc12_accel_skewness",
        "mfcc12_accel_mean",
        "mfcc8_accel_skewness",
        "mfcc8_vel_skewness",
        "mfcc13_accel_var",
        "mfcc5_vel_var",
        "mfcc6_var",
        "mfcc13_kurtosis",
        "mfcc11_mean",
        "mfcc12_accel_var",
        "mfcc10_vel_var",
        "mfcc8_vel_mean",
        "mfcc8_mean",
        "mfcc10_accel_skewness",
        "mfcc6_accel_var",
        "mfcc12_vel_skewness",
        "mfcc4_accel_var",
        "mfcc13_vel_kurtosis",
        "mfcc11_accel_kurtosis",
        "mfcc10_accel_var",
        "mfcc9_kurtosis",
        "mfcc3_vel_mean",
        "mfcc11_vel_var",
        "mfcc13_skewness",
        "mfcc9_accel_skewness",
        "mfcc6_accel_mean",
        "mfcc5_vel_kurtosis",
        "mfcc4_accel_mean",
        "mfcc3_accel_mean",
        "mfcc10_accel_mean",
        "mfcc9_accel_var",
        "mfcc3_var",
        "mfcc13_vel_mean",
        "mfcc13_var",
        "mfcc2_kurtosis",
        "mfcc9_accel_mean",
        "mfcc6_kurtosis",
        "mfcc9_vel_skewness",
        "mfcc13_accel_mean",
        "mfcc5_var",
        "mfcc13_accel_kurtosis",
        "mfcc11_accel_skewness",
        "mfcc13_accel_skewness",
        "mfcc4_skewness",
        "mfcc2_vel_kurtosis",
        "mfcc9_accel_kurtosis",
        "mfcc11_var",
        "mfcc7_skewness",
        "mfcc11_vel_mean",
        "mfcc3_accel_skewness",
        "mfcc_kurtosis",
        "mfcc7_accel_skewness",
        "mfcc3_vel_kurtosis",
        "mfcc2_skewness",
        "mfcc11_accel_mean",
        "mfcc9_vel_kurtosis",
        "mfcc4_vel_mean",
        "mfcc3_kurtosis",
        "mfcc9_vel_var",
        "mfcc8_accel_mean",
        "mfcc12_var",
        "mfcc5_vel_skewness",
        "mfcc13_vel_skewness",
        "mfcc10_vel_skewness",
        "mfcc3_vel_skewness",
        "mfcc1_accel_kurtosis",
        "mfcc10_var",
        "mfcc8_accel_var",
        "energy_accel_mean",
        "energy_vel_mean",
        "energy_accel_var",
        "energy_skewness",
        "energy_vel_skewness",
        "energy_kurtosis",
        "energy_vel_kurtosis",
        "energy_mean",
        "energy_var",
        "energy_vel_var",
        "ff_var",
        "energy_accel_skewness",
        "energy_accel_kurtosis",
        "ff_mean"
    ]


def parts_of_speech_features():
    return [
        "NumNouns",
        "NumVerbs",
        "NumberOfNID",
        "MeanWordLength",
        "NumAdverbs",
        "NumAdjectives",
        "NumDeterminers",
        "NumInterjections",
        "NumInflectedVerbs",
        "NumCoordinateConjunctions",
        "NumSubordinateConjunctions",
        "RatioNoun",
        "RatioVerb",
        "RatioPronoun",
        "RatioCoordinate",
        "getLightVerbCount",
    ]


def information_content_features():
    return [
        "keywordIUObjectCookie",
        "keywordIUObjectCupboard",
        "keywordIUObjectCurtains",
        "keywordIUObjectDishcloth",
        "keywordIUObjectDishes",
        "keywordIUObjectJar",
        "keywordIUObjectPlate",
        "keywordIUObjectSink",
        "keywordIUObjectStool",
        "keywordIUObjectWater",
        "keywordIUObjectWindow",
        "keywordIUPlaceExterior",
        "keywordIUPlaceKitchen",
        "keywordIUSubjectBoy",
        "keywordIUSubjectGirl",
        "keywordIUSubjectWoman",
        "keywordIUActionBoyTaking",
        "keywordIUActionStoolFalling",
        "keywordIUActionWaterOverflowing",
        "keywordIUActionWomanDryingWashing",
        "binaryIUActionBoyTaking",
        "binaryIUActionStoolFalling",
        "binaryIUActionWaterOverflowing",
        "binaryIUActionWomanDryingWashing",
        "binaryIUObjectCookie",
        "binaryIUObjectCupboard",
        "binaryIUObjectCurtains",
        "binaryIUObjectDishcloth",
        "binaryIUObjectDishes",
        "binaryIUObjectJar",
        "binaryIUObjectPlate",
        "binaryIUObjectSink",
        "binaryIUObjectStool",
        "binaryIUObjectWater",
        "binaryIUObjectWindow",
        "binaryIUPlaceExterior",
        "binaryIUPlaceKitchen",
        "binaryIUSubjectBoy",
        "binaryIUSubjectGirl",
        "binaryIUSubjectWoman",
    ]


def demographic_features():
    return [
        "age",
    ]


def leftSide_keyword_features():
    return [
        "ls_count",
        "ls_kw_to_w_ratio",
        "ls_ty_to_tok_ratio",
        "Right_ls_uttered",
    ]


def rightside_keyword_features():
    return [
        "prcnt_rs_uttered",
        "rs_count",
        "rs_kw_to_w_ratio",
        "rs_ty_to_tok_ratio",
    ]


def halves_features():
    return [
        "ls_count",
        "ls_kw_to_w_ratio",
        "ls_ty_to_tok_ratio",
        "prcnt_ls_uttered",
        "prcnt_rs_uttered",
        "rs_count",
        "rs_kw_to_w_ratio",
        "rs_ty_to_tok_ratio",
        # "count_ls_rs_switches"
    ]


def strips_features():
    return [
        "centerleft_count",
        "centerleft_kw_to_w_ratio",
        "centerleft_ty_to_tok_ratio",
        "centerright_count",
        "centerright_kw_to_w_ratio",
        "centerright_ty_to_tok_ratio",
        "farleft_count",
        "farleft_kw_to_w_ratio",
        "farleft_ty_to_tok_ratio",
        "farright_count",
        "farright_kw_to_w_ratio",
        "farright_ty_to_tok_ratio",
        "prcnt_centerleft_uttered",
        "prcnt_centerright_uttered",
        "prcnt_farleft_uttered",
        "prcnt_farright_uttered",
    ]


def centerleft_features():
    return [
        "centerleft_count",
        "centerleft_kw_to_w_ratio",
        "centerleft_ty_to_tok_ratio",
        "prcnt_centerleft_uttered",
    ]


def centerright_features():
    return [
        "centerright_count",
        "centerright_kw_to_w_ratio",
        "centerright_ty_to_tok_ratio",
        "prcnt_centerright_uttered",
    ]


def farleft_features():
    return [
        "farleft_count",
        "farleft_kw_to_w_ratio",
        "farleft_ty_to_tok_ratio",
        "prcnt_farleft_uttered",
    ]


def farright_features():
    return [
        "farright_count",
        "farright_kw_to_w_ratio",
        "farright_ty_to_tok_ratio",
        "prcnt_farright_uttered",
    ]


def quadrant_features():
    return [
        "NE_count",
        "NE_kw_to_w_ratio",
        "NE_ty_to_tok_ratio",
        "NW_count",
        "NW_kw_to_w_ratio",
        "NW_ty_to_tok_ratio",
        "SE_count",
        "SE_kw_to_w_ratio",
        "SE_ty_to_tok_ratio",
        "SW_count",
        "SW_kw_to_w_ratio",
        "SW_ty_to_tok_ratio",
        "prcnt_NE_uttered",
        "prcnt_NW_uttered",
        "prcnt_SE_uttered",
        "prcnt_SW_uttered",
    ]


def NE_features():
    return [
        "NE_count",
        "NE_kw_to_w_ratio",
        "NE_ty_to_tok_ratio",
        "prcnt_NE_uttered",
    ]


def NW_features():
    return [
        "NW_count",
        "NW_kw_to_w_ratio",
        "NW_ty_to_tok_ratio",
        "prcnt_NW_uttered",
    ]


def SE_features():
    return [
        "SE_count",
        "SE_kw_to_w_ratio",
        "SE_ty_to_tok_ratio",
        "prcnt_SE_uttered",
    ]


def SW_features():
    return [
        "SW_count",
        "SW_kw_to_w_ratio",
        "SW_ty_to_tok_ratio",
        "prcnt_SW_uttered",
    ]


def task_specific_features():
    new = []
    new += halves_features()
    new += strips_features()
    new += quadrant_features()
    new += information_content_features()
    return new

def make_polynomial_names(cols):
    names = []
    for f1, f2 in itertools.combinations_with_replacement(cols, 2):
        if f1 == f2:
            prefix = 'sqr_'
        else:
            prefix = 'intr_'
        name = prefix + f1 + "_" + f2
        names += [name]

    return names + cols
