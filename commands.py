
from ANFPWebScraper import ScotiabankTournament
from jinja2 import Template


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me!"
    )


def get_statistics(bot, update):
    tournament = ScotiabankTournament()
    stats = tournament.get_statistics()
    template = Template('''
        - {{ CLUB }}
        PJ:{{ PJ }} PG:{{ PG }} PP:{{ PP }} PE:{{ PE }} GF:{{ GF }} GC:{{ GC }}
        Posicion: {{ POS }}
        Puntos: {{ PTS }}
        Diferencia: {{ DIF }}
        ''')
    for team in stats:
        bot.send_message(
            chat_id=update.message.chat_id,
            text=template.render(
                team
            )
        )
