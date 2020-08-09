import pickle
import pandas as pd
import numpy as np

# read in the model
my_model = pickle.load(open("my_pickled_model.p","rb"))

# create a function to take in user-entered amounts and apply the model
def win_or_lose(amounts_float, model=my_model):
    
    # amounts_float[0] = 2400.0
    # amounts_float[1] = 1.0
    # amounts_float[2] = 0.0
    # amounts_float[3] = 0.0
    # amounts_float[4] = 0.0
    # amounts_float[5] = 0.0
    # amounts_float[6] = 0.0
    # amounts_float[7] = 0.0
    # amounts_float[8] = 0.0
    # amounts_float[9] = 0.0
    # amounts_float[10] = 0.0
    # amounts_float[11] = 0.0
    # amounts_float[12] = 0.0
    # amounts_float[13] = 0.0
    # amounts_float[14] = 0.0
    # amounts_float[15] = 0.0
    # amounts_float[16] = 0.0
    # amounts_float[17] = 0.0
    # amounts_float[18] = 0.0
    # amounts_float[19] = 0.0
    # amounts_float[20] = 0.0
    # amounts_float[21] = 0.0
    # amounts_float[22] = 0.0
    # amounts_float[23] = 0.0
    # amounts_float[24] = 0.0
    # amounts_float[25] = 0.0
    # amounts_float[26] = 0.0
    # amounts_float[27] = 0.0
    # amounts_float[28] = 0.0
    # amounts_float[29] = 0.0
    # amounts_float[30] = 0.0
    # amounts_float[31] = 0.0
    # amounts_float[32] = 0.0
    # amounts_float[33] = 0.0
    # amounts_float[34] = 0.0
    # amounts_float[35] = 0.0
    # amounts_float[36] = 0.0
    # amounts_float[37] = 0.0
    # amounts_float[38] = 0.0
    # amounts_float[39] = 0.0
    # amounts_float[40] = 0.0
    # amounts_float[41] = 0.0
    # amounts_float[42] = 0.0
    # amounts_float[43] = 0.0
    # amounts_float[44] = 0.0
    # amounts_float[45] = 0.0
    # amounts_float[46] = 0.0
    # amounts_float[47] = 0.0
    # amounts_float[48] = 0.0
    # amounts_float[49] = 0.0
    # amounts_float[50] = 0.0
    # amounts_float[51] = 0.0
    # amounts_float[52] = 0.0
    # amounts_float[53] = 0.0
    # amounts_float[54] = 0.0
    # amounts_float[55] = 0.0
    # amounts_float[56] = 0.0
    # amounts_float[57] = 0.0
    # amounts_float[58] = 0.0
    # amounts_float[59] = 0.0
    # amounts_float[60] = 0.0
    # amounts_float[61] = 0.0
    # amounts_float[62] = 0.0
    # amounts_float[63] = 0.0
    # amounts_float[64] = 0.0
    # amounts_float[65] = 0.0
    # amounts_float[66] = 0.0
    # amounts_float[67] = 0.0
    # amounts_float[68] = 0.0
    # amounts_float[69] = 0.0
    # amounts_float[70] = 0.0
    # amounts_float[71] = 0.0
    # amounts_float[72] = 0.0
    # amounts_float[73] = 0.0
    # amounts_float[74] = 0.0
    # amounts_float[75] = 0.0
    # amounts_float[76] = 0.0
    # amounts_float[77] = 0.0
    # amounts_float[78] = 0.0
    # amounts_float[79] = 0.0
    # amounts_float[80] = 0.0
    # amounts_float[81] = 0.0
    # amounts_float[82] = 0.0
    # amounts_float[83] = 0.0
    # amounts_float[84] = 0.0
    # amounts_float[85] = 0.0
    # amounts_float[86] = 0.0
    # amounts_float[87] = 0.0
    # amounts_float[88] = 0.0
    # amounts_float[89] = 0.0
    # amounts_float[90] = 0.0
    # amounts_float[91] = 0.0
    # amounts_float[92] = 0.0
    # amounts_float[93] = 0.0
    # amounts_float[94] = 0.0
    # amounts_float[95] = 0.0
    # amounts_float[96] = 0.0
    # amounts_float[97] = 0.0
    # amounts_float[98] = 0.0
    # amounts_float[99] = 0.0
    # amounts_float[100] = 0.0
    # amounts_float[101] = 0.0
    # amounts_float[102] = 0.0
    # amounts_float[103] = 0.0
    # amounts_float[104] = 0.0
    # amounts_float[105] = 0.0
    # amounts_float[106] = 0.0
    
    # gameDuration = 2400.0
    # level = 1.0
    # Ahri_items = 0.0
    # Ahri_star = 0.0
    # Annie_items = 0.0
    # Annie_star = 0.0
    # Ashe_items = 0.0
    # Ashe_star = 0.0
    # AurelionSol_items = 0.0
    # AurelionSol_star = 0.0
    # Blitzcrank_items = 0.0
    # Blitzcrank_star = 0.0
    # Caitlyn_items = 0.0
    # Caitlyn_star = 0.0
    # ChoGath_items = 0.0
    # ChoGath_star = 0.0
    # Darius_items = 0.0
    # Darius_star = 0.0
    # Ekko_items = 0.0
    # Ekko_star = 0.0
    # Ezreal_items = 0.0
    # Ezreal_star = 0.0
    # Fiora_items = 0.0
    # Fiora_star = 0.0
    # Fizz_items = 0.0
    # Fizz_star = 0.0
    # Gangplank_items = 0.0
    # Gangplank_star = 0.0
    # Graves_items = 0.0
    # Graves_star = 0.0
    # Irelia_items = 0.0
    # Irelia_star = 0.0
    # JarvanIV_items = 0.0
    # JarvanIV_star = 0.0
    # Jayce_items = 0.0
    # Jayce_star = 0.0
    # Jhin_items = 0.0
    # Jhin_star = 0.0
    # Jinx_items = 0.0
    # Jinx_star = 0.0
    # KaiSa_items = 0.0
    # KaiSa_star = 0.0
    # Karma_items = 0.0
    # Karma_star = 0.0
    # Kassadin_items = 0.0
    # Kassadin_star = 0.0
    # Kayle_items = 0.0
    # Kayle_star = 0.0
    # KhaZix_items = 0.0
    # KhaZix_star = 0.0
    # Leona_items = 0.0
    # Leona_star = 0.0
    # Lucian_items = 0.0
    # Lucian_star = 0.0
    # Lulu_items = 0.0
    # Lulu_star = 0.0
    # Lux_items = 0.0
    # Lux_star = 0.0
    # Malphite_items = 0.0
    # Malphite_star = 0.0
    # MasterYi_items = 0.0
    # MasterYi_star = 0.0
    # MissFortune_items = 0.0
    # MissFortune_star = 0.0
    # Mordekaiser_items = 0.0
    # Mordekaiser_star = 0.0
    # Neeko_items = 0.0
    # Neeko_star = 0.0
    # Poppy_items = 0.0
    # Poppy_star = 0.0
    # Rakan_items = 0.0
    # Rakan_star = 0.0
    # Rumble_items = 0.0
    # Rumble_star = 0.0
    # Shaco_items = 0.0
    # Shaco_star = 0.0
    # Shen_items = 0.0
    # Shen_star = 0.0
    # Sona_items = 0.0
    # Sona_star = 0.0
    # Soraka_items = 0.0
    # Soraka_star = 0.0
    # Syndra_items = 0.0
    # Syndra_star = 0.0
    # Thresh_items = 0.0
    # Thresh_star = 0.0
    # TwistedFate_items = 0.0
    # TwistedFate_star = 0.0
    # VelKoz_items = 0.0
    # VelKoz_star = 0.0
    # Vi_items = 0.0
    # Vi_star = 0.0
    # WuKong_items = 0.0
    # WuKong_star = 0.0
    # Xayah_items = 0.0
    # Xayah_star = 0.0
    # Xerath_items = 0.0
    # Xerath_star = 0.0
    # XinZhao_items = 0.0
    # XinZhao_star = 0.0
    # Yasuo_items = 0.0
    # Yasuo_star = 0.0
    # Ziggs_items = 0.0
    # Ziggs_star = 0.0
    # Zoe_items = 0.0 
    # Zoe_star = 0.0

    # inputs into the model
    input_df = [[amounts_float[0], amounts_float[1], amounts_float[2], amounts_float[3], amounts_float[4], amounts_float[5],
                 amounts_float[6], amounts_float[7], amounts_float[8], amounts_float[9], amounts_float[10], amounts_float[11],
                 amounts_float[12], amounts_float[13], amounts_float[14], amounts_float[15], amounts_float[16], amounts_float[17],
                  amounts_float[18], amounts_float[19], amounts_float[20], amounts_float[21], amounts_float[22], amounts_float[23],
                  amounts_float[24], amounts_float[25], amounts_float[26], amounts_float[27], amounts_float[28], amounts_float[29],
                  amounts_float[30], amounts_float[31], amounts_float[32], amounts_float[33], amounts_float[34], amounts_float[35],
                  amounts_float[36], amounts_float[37], amounts_float[38], amounts_float[39], amounts_float[40], amounts_float[41],
                  amounts_float[42], amounts_float[43], amounts_float[44], amounts_float[45], amounts_float[46], amounts_float[47],
                  amounts_float[48], amounts_float[49], amounts_float[50], amounts_float[51], amounts_float[52], amounts_float[53],
                  amounts_float[54], amounts_float[55], amounts_float[56], amounts_float[57], amounts_float[58], amounts_float[59],
                  amounts_float[60], amounts_float[61], amounts_float[62], amounts_float[63], amounts_float[64], amounts_float[65],
                  amounts_float[66], amounts_float[67], amounts_float[68], amounts_float[69], amounts_float[70], amounts_float[71],
                  amounts_float[72], amounts_float[73], amounts_float[74], amounts_float[75], amounts_float[76], amounts_float[77],
                  amounts_float[78], amounts_float[79], amounts_float[80], amounts_float[81], amounts_float[82], amounts_float[83],
                  amounts_float[84], amounts_float[85], amounts_float[86], amounts_float[87], amounts_float[88], amounts_float[89],
                  amounts_float[90], amounts_float[91], amounts_float[92], amounts_float[93], amounts_float[94], amounts_float[95],
                  amounts_float[96], amounts_float[97], amounts_float[98], amounts_float[99], amounts_float[100], amounts_float[101],
                  amounts_float[102], amounts_float[103], amounts_float[104], amounts_float[105]]]
    # input_df = [[gameDuration, level, Ahri_items, Ahri_star, Annie_items, Annie_star,
    #              Ashe_items, Ashe_star, AurelionSol_items, AurelionSol_star, Blitzcrank_items,
    #              Blitzcrank_star, Caitlyn_items, Caitlyn_star, ChoGath_items, ChoGath_star,
    #              Darius_items, Darius_star, Ekko_items, Ekko_star, Ezreal_items, Ezreal_star,
    #              Fiora_items, Fiora_star, Fizz_items, Fizz_star, Gangplank_items, Gangplank_star,
    #              Graves_items, Graves_star, Irelia_items, Irelia_star, JarvanIV_items,
    #              JarvanIV_star, Jayce_items, Jayce_star, Jhin_items, Jhin_star, Jinx_items,
    #              Jinx_star, KaiSa_items, KaiSa_star, Karma_items, Karma_star, Kassadin_items,
    #              Kassadin_star, Kayle_items, Kayle_star, KhaZix_items, KhaZix_star, Leona_items,
    #              Leona_star, Lucian_items, Lucian_star, Lulu_items, Lulu_star, Lux_items,
    #              Lux_star, Malphite_items, Malphite_star, MasterYi_items, MasterYi_star,
    #              MissFortune_items, MissFortune_star, Mordekaiser_items, Mordekaiser_star,
    #              Neeko_items, Neeko_star, Poppy_items, Poppy_star, Rakan_items, Rakan_star,
    #              Rumble_items, Rumble_star, Shaco_items, Shaco_star, Shen_items, Shen_star,
    #              Sona_items, Sona_star, Soraka_items, Soraka_star, Syndra_items, Syndra_star,
    #              Thresh_items, Thresh_star, TwistedFate_items, TwistedFate_star, VelKoz_items,
    #              VelKoz_star, Vi_items, Vi_star, WuKong_items, WuKong_star, Xayah_items,
    #              Xayah_star, Xerath_items, Xerath_star, XinZhao_items, XinZhao_star, Yasuo_items,
    #              Yasuo_star, Ziggs_items, Ziggs_star, Zoe_items, Zoe_star]]

    # make a prediction
    x_array = np.array(input_df)
    x_array = x_array.reshape(1,106)
    prediction = my_model.predict_proba(x_array)[:,1]

    # return a message
    thresh_num = 0.41594769254609176
    if prediction > thresh_num:
        predictY = 'Win'
    else:
        predictY = 'Lose'
        
    prob_per = np.round_(prediction*100, 2)
    
    result = "You have a {1}% to win, which means you're more likely to {0}.".format(predictY, prob_per)

    return result
