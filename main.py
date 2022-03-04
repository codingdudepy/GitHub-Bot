import discord
import requests
from discord.ext import commands
import base64
from github import Github


#intializing discord bot and setting prefix
client = commands.Bot(command_prefix='!')

@client.command()
async def getdata(ctx):
  def check(message):
      return message.author == ctx.author and message.channel == ctx.channel

  await ctx.send('Please enter the username to there github')
  title = await client.wait_for('message', check=check)
  url = f"https://api.github.com/users/{title.content}"
  user_data = requests.get(url).json()
  bio = (str(user_data["bio"]))
  followers = (int(user_data["followers"]))
  following = (int(user_data["following"]))
  public = (str(user_data["public_repos"]))
  company = (str(user_data["company"]))
  id = (int(user_data["id"]))
  avatar = (str(user_data["avatar_url"]))
  twitter = (str(user_data["twitter_username"]))
  blog = (str(user_data["blog"]))
  location = (str(user_data["location"]))
  await ctx.send(f"Bio: {bio}\nFollowers: {followers}\nFollowing: {following}\nAmount of public repos: {public}\nCompany: {company}\nID: {id}\nTwitter: {twitter}\nBlog: {blog}\nLocation: {location}\nAvatar URL: {avatar}")


@client.command()
async def getrepos(ctx):
  def check(message):
    return message.author == ctx.author and message.channel == ctx.channel

  await ctx.send("Please enter the username to there github: ")
  title = await client.wait_for('message', check=check)
  username = f"{title.content}"
  g = Github()
  user = g.get_user(username)
  items = []
  for repo in user.get_repos():
    await ctx.send(repo)

   



client.run(token)
