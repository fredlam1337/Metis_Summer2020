from flask import Flask, request, render_template
from make_prediction import win_or_lose

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_tft/', methods=['GET', 'POST'])
def render_message():

    # user-entered features
    features = ['gameDuration', 'level', 'Ahri_items', 'Ahri_star', 'Annie_items', 'Annie_star',
                'Ashe_items', 'Ashe_star', 'AurelionSol_items', 'AurelionSol_star', 'Blitzcrank_items',
                'Blitzcrank_star', 'Caitlyn_items', 'Caitlyn_star', 'ChoGath_items', 'ChoGath_star',
                'Darius_items', 'Darius_star', 'Ekko_items', 'Ekko_star', 'Ezreal_items', 'Ezreal_star',
                'Fiora_items', 'Fiora_star', 'Fizz_items', 'Fizz_star', 'Gangplank_items', 'Gangplank_star',
                'Graves_items', 'Graves_star', 'Irelia_items', 'Irelia_star', 'JarvanIV_items',
                'JarvanIV_star', 'Jayce_items', 'Jayce_star', 'Jhin_items', 'Jhin_star', 'Jinx_items',
                'Jinx_star', 'KaiSa_items', 'KaiSa_star', 'Karma_items', 'Karma_star', 'Kassadin_items',
                'Kassadin_star', 'Kayle_items', 'Kayle_star', 'KhaZix_items', 'KhaZix_star', 'Leona_items',
                'Leona_star', 'Lucian_items', 'Lucian_star', 'Lulu_items', 'Lulu_star', 'Lux_items',
                'Lux_star', 'Malphite_items', 'Malphite_star', 'MasterYi_items', 'MasterYi_star',
                'MissFortune_items', 'MissFortune_star', 'Mordekaiser_items', 'Mordekaiser_star',
                'Neeko_items', 'Neeko_star', 'Poppy_items', 'Poppy_star', 'Rakan_items', 'Rakan_star',
                'Rumble_items', 'Rumble_star', 'Shaco_items', 'Shaco_star', 'Shen_items', 'Shen_star',
                'Sona_items', 'Sona_star', 'Soraka_items', 'Soraka_star', 'Syndra_items', 'Syndra_star',
                'Thresh_items', 'Thresh_star', 'TwistedFate_items', 'TwistedFate_star', 'VelKoz_items', 
                'VelKoz_star', 'Vi_items', 'Vi_star', 'WuKong_items', 'WuKong_star', 'Xayah_items',
                'Xayah_star', 'Xerath_items', 'Xerath_star', 'XinZhao_items', 'XinZhao_star', 'Yasuo_items',
                'Yasuo_star', 'Ziggs_items', 'Ziggs_star', 'Zoe_items', 'Zoe_star']

    # error messages to ensure correct units of measure
    message = "That's not a number."

    # hold all amounts as floats
    values = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(features):
        user_input = request.form[ing]
        try:
            float_value = float(user_input)
        except:
            return render_template('index.html', message=message)
        values.append(float_value)

    # show user final message
    final_message = win_or_lose(values)
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)