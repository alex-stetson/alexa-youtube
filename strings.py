# -*- coding: utf-8 -*-

# To run as an Alexa hosted skill:
# 1. Uncomment lines 9-14 below
# 2. Insert your Google developer key in line 10
# 3. Make sure to add this strings.py file to the lambda folder
# 4. Make sure to add pytube to the requirements.txt file in the lambda folder

#environ = {
#    "DEVELOPER_KEY": "insert_your_key_here",
#    "youtube_dl": "false",
#    "youtube_dl_error_mirror": "",
#    "AWS_LAMBDA_FUNCTION_NAME": ""
#}

locales = {
    'en-GB': 'Europe/London',
    'en-US': 'America/New York',
    'en-CA': 'America/New York',
    'en-AU': 'Australia/Sydney',
    'en-IN': 'Asia/Kolkata',
    'fr-FR': 'Europe/Paris',
    'fr-CA': 'America/New York',
    'de-DE': 'Europe/Berlin',
    'it-IT': 'Europe/Rome',
    'es-ES': 'Europe/Madrid',
    'es-MX': 'America/Mexico City',
    'ja-JP': 'Asia/Tokyo',
    'pt-BR': 'Brasil/Sao Paulo'
}

strings_en = {
'welcome1':"Welcome to Youtube. Say, for example, play videos by The Beatles.",
'welcome2':"Or you can say, shuffle songs by Michael Jackson.",
'help':"For example say, play videos by Fall Out Boy",
'illegal':"You can't do that with this skill.",
'gonewrong':"Sorry, something's gone wrong",
'playlist':"The playlist",
'channel':"The channel",
'video':"The video",
'notworked':"hasn't worked, shall I try the next one?",
'playing':"Playing",
'pausing':"Pausing",
'nomoreitems':"There are no more items in the playlist.",
'resuming':"Resuming",
'noresume':"I wasn't able to resume playing.",
'novideo':"I wasn't able to play a video.",
'notitle':"I can't find out the name of the current video.",
'nowplaying':"Now playing",
'nothingplaying':"Nothing is currently playing.",
'sorryskipby':"Sorry, I didn't hear how much to skip by",
'sorryskipto':"Sorry, I didn't hear where to skip to",
'ok':"OK",
'currentposition':"The current position is",
'hours':"hours",
'hour':"hour",
'minutes':"minutes",
'minute':"minute",
'seconds':"seconds",
'second':"second",
'throttled':"This skill is being throttled by YouTube, please try again later.",
'error403':"Sorry, this skill has hit it's usage limit for today.",
'apikeyerror':"Sorry, there was a problem with the Youtube API key.",
'youtubeerror':"There was a problem with the youtube search response.",
'nochannelid':"You do not have a channel id set.",
}
strings_fr = {
'welcome1':"Bienvenue sur Youtube. Dite, par exemple, jouer une vidéo de Madonna.",
'welcome2':"Ou vous pouvez dire, chanson aléatoire de Michael Jackson.",
'help':"Par exemple dite, joue une vidéo de Michael Jackson",
'illegal':"Vous ne pouvez pas faire ça avec cette skill.",
'gonewrong':"Désolé, quelque chose n'a pas fonctionné",
'playlist':"La playlist",
'channel':"La chaîne",
'video':"The vidéo",
'notworked':"ne fonctionne pas, dois je essayer la suivante ?",
'playing':"Lecture de",
'pausing':"En pause",
'nomoreitems':"Il n'y a plus rien à lire dans cette playlist.",
'resuming':"Reprise",
'noresume':"Je n'ai pas pu reprendre la lecture.",
'novideo':"Je ne peux pas lire la vidéo.",
'notitle':"Je ne retrouve pas le nom de cette vidéo.",
'nowplaying':"Vous écoutez ",
'nothingplaying':"Il n'y a aucune lecture en cours.",
'sorryskipby':"Désolé, je n'ai pas compris de combien je devais avancer ou reculer.",
'sorryskipto':"Désolé, je n'ai pas compris de combien je devais avancer ou reculer.",
'ok':"OK",
'currentposition':"La position actuelle est",
'hours':"heures",
'hour':"heure",
'minutes':"minutes",
'minute':"minute",
'seconds':"secondes",
'second':"seconde",
}
strings_it = {
'welcome1':"Benvenuto su YouTube. Dì, per esempio, riproduci video dei Beatles.",
'welcome2':"Oppure puoi dire, canzoni casuali di Michael Jackson.",
'help':"Per esempio dì, riproduci i video dei Fall out Boy",
'illegal':"Non puoi fare questo con questa skill.",
'gonewrong':"Spiacente, qualcosa è andato storto",
'playlist':"La playlist",
'channel':"Il canale",
'video':"Il video",
'notworked':"non ha funzionato, dovrei provare la prossima?",
'playing':"Riproduco",
'pausing':"Ciao da Youtube",
'nomoreitems':"Non ci sono più elementi nella playlist.",
'resuming':"Riprendo",
'noresume':"Non ero in grado di riprendere il video.",
'novideo':"Non ero in grado di riprodurre un video",
'notitle':"Non riesco a trovare il nome del video corrente.",
'nowplaying':"Ora riproduco",
'nothingplaying':"Al momento non sto riproducendo nulla.",
'sorryskipby':"Spiacente, non ho capito di quanto saltare",
'sorryskipto':"Spiacente, non ho capito dove saltare",
'ok':"OK",
'currentposition':"La posizione attuale è",
'hours':"ore",
'hour':"ora",
'minutes':"minuti",
'minute':"minuto",
'seconds':"secondi",
'second':"secondo",
}
strings_de = {
'welcome1':"Herzlich willkommen bei Youtube. Was kann ich für Dich tun? Sage zum Beispiel 'spiel Videos von The Beatles'.",
'welcome2':"Oder sag misch Songs von Michael Jackson.",
'help':"Sag zum Beispiel 'spiel Videos von Fall Out Boy ab' um Videos von Fall Out Boy abzuspielen.",
'illegal':"Das kannst Du mit diesen Skill nicht tun.",
'gonewrong':"Das tut mir Leid, das hat nicht funktioniert",
'playlist':"Die Wiedergabeliste",
'channel':"Der Kanal",
'video':"Das Video",
'notworked':"hat nicht funktioniert, soll ich das nächste Element versuchen?",
'playing':"Spiele",
'pausing':"Pausieren",
'nomoreitems':"Die Wiedergabeliste enthält keine weiteren Elemente.",
'resuming':"Fortsetzen",
'noresume':"Leider konnte ich nicht weiter spielen.",
'novideo':"Dieses Video konnte ich nicht abspielen.",
'notitle':"Ich kann den Namen des aktuellen Videos nicht finden.",
'nowplaying':"Es läuft gerade",
'nothingplaying':"Es wird momentan kein Song abgespielt.",
'sorryskipby':"Entschuldigung, ich habe nicht verstanden, wie viel ich überspringen soll",
'sorryskipto':"Entschuldigung, ich habe nicht verstanden, wohin ich springen soll",
'ok':"OK",
'currentposition':"Die aktuelle Position ist",
'hours':"Stunden",
'hour':"Stunde",
'minutes':"Minuten",
'minute':"Minute",
'seconds':"Sekunden",
'second':"Sekunde",
}
strings_es = {
'welcome1':"Bienvenido a Youtube. Di, por ejemplo, pon canciones de Mozart.",
'welcome2':"O puedes decir, canciones en aleatorio de Vivaldi.",
'help':"Por ejemplo di, pon un vídeo de Relajación. O pon una lista aleatoria de sonidos de lluvia.",
'illegal':"No puedes hacer eso con esta skill.",
'gonewrong':"Lo siento, ha ocurrido un error.",
'playlist':"La playlist",
'channel':"El canal",
'video':"El vídeo",
'notworked':"No ha funcionado, pruebo con la siguiente?",
'playing':"Sonando",
'pausing':"Para.",
'nomoreitems':"No hay mas items en la playlist.",
'resuming':"Resumiendo.",
'noresume':"No es posible continuar.",
'novideo':"No se puede reproducir el vídeo.",
'notitle':"No puedo encontrar el título del vídeo.",
'nowplaying':"Ahora suena",
'nothingplaying':"No está sonando nada.",
'sorryskipby':"Lo siento, no he oído cuanto adelantar.",
'sorryskipto':"Lo siento, no he oído a donde adelantar.",
'ok':"OK",
'currentposition':"La posición actual es",
'hours':"horas",
'hour':"hora",
'minutes':"minutos",
'minute':"minuto",
'seconds':"segundos",
'second':"segundo",
}
strings_ja = {
'welcome1':"ユーチューブへようこそ.  例えば, ｢ビートルズのビデオを再生｣ と話しかけてください.",
'welcome2':"それとも, ｢マイケル・ジャクソンの曲をシャッフル再生｣ と話しかけてください.",
'help':"例えば, マイケル・ジャクソンの曲をシャッフル再生と話しかけてください.",
'illegal':"このスキルはその動作に対応しておりません.",
'gonewrong':"すいません, なにか問題が起きたようです.",
'playlist':"プレイリスト",
'channel':"チャンネル",
'video':"動画",
'notworked':"は正常に動作しませんでした. 次を試しますか?",
'playing':"再生中",
'pausing':"停止中",
'nomoreitems':"プレイリストにこれ以上動画はありません.",
'resuming':"再開中",
'noresume':"再生を再開できませんでした.",
'novideo':"動画を再生できませんでした.",
'notitle':"現在再生中の動画の名前はわかりませんでした.",
'nowplaying':"再生中",
'nothingplaying':"現在何も流れていません.",
'sorryskipby':"すいません. どれだけスキップするか聞き取れませんでした.",
'sorryskipto':"すいません. どこまでスキップするか聞き取れませんでした.",
'ok':"はい.",
'currentposition':"現在の再生位置は,",
'hours':"時間",
'hour':"時間",
'minutes':"分",
'minute':"分",
'seconds':"秒",
'second':"秒",
}
strings_pt = {
'welcome1':"Bem vindo ao Youtube. Diga, por exemplo, toque um vídeo dos Beatles.",
'welcome2':"Ou você pode dizer, toque músicas de Michael Jackson.",
'help':"Por exemplo, diga, toque vídeos de Fall Out Boy",
'illegal':"Você não pode fazer isso com essa skill.",
'gonewrong':"Desculpe, algo deu errado",
'playlist':"A playlist",
'channel':"O canal",
'video':"O vídeo",
'notworked':"não funcionou, devo tentar o próximo?",
'playing':"Tocando",
'pausing':"Pausando",
'nomoreitems':"Existem mais itens na playlist.",
'resuming':"Retomando",
'noresume':"Não consegui voltar a tocar.",
'novideo':"Não consegui tocar o vídeo.",
'notitle':"Não encontrei o nome do vídeo atual.",
'nowplaying':"Tocando agora",
'nothingplaying':"Nada está tocando atualmente.",
'sorryskipby':"Desculpe, não ouvi quanto tenho que pular",
'sorryskipto':"Desculpe, não entendi para onde tenho que pular",
'ok':"OK",
'currentposition':"A posição atual é",
'hours':"horas",
'hour':"hora",
'minutes':"minutos",
'minute':"minuto",
'seconds':"segundos",
'second':"segundo",
}
