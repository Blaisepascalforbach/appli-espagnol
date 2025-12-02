<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Vidéo Robson Square - Sous-titrée FR</title>
    <style>
        body { font-family: sans-serif; background: #222; color: white; display: flex; flex-direction: column; align-items: center; padding: 20px; }
        h2 { margin-bottom: 10px; }
        #video-container { position: relative; width: 640px; height: 360px; margin-bottom: 20px; }
        #subtitle-box {
            width: 600px;
            min-height: 80px;
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #444;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-size: 18px;
            line-height: 1.5;
            color: #ffd700; /* Jaune pour la lisibilité */
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }
        .hint { font-size: 0.8em; color: #ccc; margin-top: 10px; }
    </style>
</head>
<body>

    <h2>Traduction Française Synchronisée</h2>

    <div id="player"></div>

    <div id="subtitle-box">Les sous-titres apparaîtront ici une fois la vidéo lancée...</div>
    
    <p class="hint">Note : Si la vidéo ne démarre pas, cliquez dessus. Les sous-titres sont synchronisés automatiquement.</p>

    <script>
        // 1. Charge l'API IFrame Player API de manière asynchrone.
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        var player;
        var subtitleBox = document.getElementById('subtitle-box');
        var timer;

        // 2. Les données de sous-titres (Temps en secondes : Texte)
        const subtitles = [
            { start: 0, end: 5, text: "À 55 ans, Arthur Erickson est une superstar de l'architecture." },
            { start: 5, end: 9, text: "L'un des joyaux du portefeuille de ce regretté architecte de Vancouver est cette rampe..." },
            { start: 9, end: 14, text: "...qui zigzague à travers les marches de Robson Square, comme un sentier en lacet sur une montagne." },
            { start: 14, end: 18, text: "Le consultant en accessibilité Arnold Cheng convient que c'est beau, mais il déteste ça." },
            { start: 18, end: 22, text: "Quand vous combinez un escalier et une rampe, ils fonctionnent rarement bien ensemble," },
            { start: 22, end: 26, text: "car vous avez deux éléments concurrents ici." },
            { start: 26, end: 30, text: "Cheng affirme que le problème avec la rampe d'accès, c'est qu'elle n'est pas très accessible." },
            { start: 30, end: 35, text: "Elle est si raide que descendre en fauteuil roulant ou avec une poussette peut être dangereux." },
            { start: 35, end: 39, text: "Et pour la montée, je pense que c'est surtout une question d'endurance." },
            { start: 39, end: 43, text: "Il m'a fallu beaucoup de force pour monter, alors imaginez quelqu'un de plus âgé..." },
            { start: 43, end: 48, text: "...ou qui a moins de muscles ; il pourrait ne pas être capable de monter du tout." },
            { start: 48, end: 52, text: "La rampe n'est pas la seule plainte de Cheng." },
            { start: 52, end: 56, text: "Il peut être difficile de distinguer où finit une marche et où commence la suivante..." },
            { start: 56, end: 60, text: "...car elles sont toutes de la même couleur, surtout si vous êtes malvoyant..." },
            { start: 60, end: 64, text: "...et que le temps est couvert ou qu'il pleut. Cheng suggère de rendre la rampe moins raide," },
            { start: 64, end: 68, text: "d'ajouter plus de mains courantes et de mettre des bandes de contraste de couleur..." },
            { start: 68, end: 72, text: "...sur les marches pour améliorer la visibilité." },
            { start: 72, end: 76, text: "Les admirateurs d'Erickson disent que les marches ont été construites selon les normes," },
            { start: 76, end: 80, text: "et même il y a 40 ans, l'architecte avait l'accessibilité à l'esprit," },
            { start: 80, end: 85, text: "car son père a perdu ses deux jambes pendant la Première Guerre mondiale." },
            { start: 85, end: 90, text: "...un énorme handicap qui a évidemment eu un impact sur sa vie..." },
            { start: 90, end: 94, text: "...et sa volonté de rendre les espaces publics accessibles." },
            { start: 94, end: 99, text: "Lorsque l'architecte Jim Cheng sortait tout juste de l'université," },
            { start: 99, end: 103, text: "il a travaillé sous la direction d'Erickson sur le Robson Square." },
            { start: 103, end: 106, text: "Je suis toujours très fier de la vision d'Erickson." },
            { start: 106, end: 110, text: "Il est ouvert à des changements mineurs, mais il veut protéger la vision d'Erickson." },
            { start: 110, end: 115, text: "Peut-être est-ce acceptable de dire aux gens : « Hé, si vous n'êtes pas à l'aise avec ces rampes..." },
            { start: 115, end: 120, text: "...il y a une option pour vous, prenez l'ascenseur ». Nous avons tous le choix." },
            { start: 120, end: 125, text: "Tout changement apporté aux marches devrait être approuvé par la province." },
            { start: 125, end: 129, text: "Cheng a donc ce message pour le gouvernement de la Colombie-Britannique :" },
            { start: 129, end: 134, text: "Ce n'est pas parce qu'une chose est classée au patrimoine qu'elle ne peut pas être améliorée." },
            { start: 134, end: 139, text: "La Grande Muraille de Chine est accessible car quelqu'un a eu la vision de la rendre accessible," },
            { start: 139, end: 144, text: "...et ils n'ont pas enlevé grand-chose à l'ouvrage ; cela reste la Grande Muraille." },
            { start: 144, end: 149, text: "Cheng sait que se battre pour changer un espace aussi célèbre est un défi de taille," },
            { start: 149, end: 154, text: "...mais cela ne l'a jamais arrêté auparavant et cela ne l'arrêtera pas maintenant." },
            { start: 154, end: 160, text: "Jesse Johnston CBC News Vancouver." }
        ];

        // 3. Création du lecteur vidéo
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                height: '360',
                width: '640',
                videoId: 'Yv6izkxhAEA',
                events: {
                    'onStateChange': onPlayerStateChange
                }
            });
        }

        // 4. Boucle de synchronisation
        function onPlayerStateChange(event) {
            if (event.data == YT.PlayerState.PLAYING) {
                startSubtitleSync();
            } else {
                stopSubtitleSync();
            }
        }

        function startSubtitleSync() {
            timer = setInterval(function() {
                var currentTime = player.getCurrentTime();
                var currentSub = subtitles.find(sub => currentTime >= sub.start && currentTime < sub.end);
                
                if (currentSub) {
                    subtitleBox.innerHTML = currentSub.text;
                } else {
                    // Ne rien effacer pour laisser le dernier texte, ou mettre "..."
                    // subtitleBox.innerHTML = ""; 
                }
            }, 500); // Vérifie toutes les 0.5 secondes
        }

        function stopSubtitleSync() {
            clearInterval(timer);
        }
    </script>
</body>
</html>
