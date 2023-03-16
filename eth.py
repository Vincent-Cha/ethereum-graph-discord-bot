import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import requests
import json
import datetime

# Créer un bot Discord
bot = commands.Bot(command_prefix='!', intents = discord.Intents(messages=True, guilds=True))

# Définir la commande pour générer le graphique
@bot.command()
async def graph(ctx):
    # Récupérer les données de prix de l'ethereum depuis l'API CoinGecko
    response = requests.get("https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=1")
    prices = json.loads(response.text)["prices"]

    # Préparer les données pour le graphique
    x = [datetime.datetime.fromtimestamp(p[0]/1000) for p in prices]
    y = [p[1] for p in prices]

    # Générer le graphique
    plt.plot(x, y)
    plt.title("Prix de l'ethereum (USD) des dernières 24 heures")
    plt.xlabel("Date")
    plt.ylabel("Prix")

    # Sauvegarder le graphique et envoyer en réponse sur Discord
    plt.savefig("ethereum.png")
    await ctx.send(file=discord.File("ethereum.png"))

# Lancer le bot Discord
bot.run("Your token here !")