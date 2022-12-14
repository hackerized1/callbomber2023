// Call Bomber Discord Bot
// Java için çevirdim discord a kullanırsın star atmazsan öl amk
const Discord = require('discord.js');
const client = new Discord.Client();

client.on('message', message => {
    // Doğrulama komutu
    if (message.content.startsWith('!callbomb')) {

        // Numara al
        let args = message.content.split(' ').slice(1);
        let number = args[0];

        // Numara doğrulama
        if (!number || number.length != 10) {
            message.reply('Lütfen geçerli bir telefon numarası girin!')
        } else {
            // Numaraya arama yapılmasını sağla
            // ...
            message.reply('Numara başarıyla aranıyor.');
        }
    }
});

client.login('your-discord-bot-token');
