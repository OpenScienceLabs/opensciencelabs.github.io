---
title: Discord
slug: discord-en
date: 2019-04-08
authors: ["Ivan Ogasawara"]
---

<!--
.. title: Discord
.. slug: discord/en
.. date: 2019-04-08
.. authors: ["Ivan Ogasawara"]
.. tags: devops, discord
.. category: devops
.. link:
.. description:
..
-->

<!-- # [EN] Discord -->

Discord is our main comunication tool for our community. The direct link
to our discord is [http://discord.opensciencelabs.org](opensciencelabs.org/discord).

## Conventions

Each channel has a unique name with a prefix, according to the category. For example,
a channel inside the category Python starts with the prefix `py-`.

Some category name are long and some times it is hard to find a prefix for that.
But, it is important that the prefix has some relation to the category.

## Configuration

TBD

## Bots

We use bots to help us to maintain our server.

### MEE6

For ranking we are using **MEE6**. We don't have any activity our any rewards using the
ranking score, but maybe in the future we can use it.


### Dyno

**Dyno bot** is used for maintainance tasks, such as:

- welcome message
- ban users
- block users
- etc (TODO: add all the options used)

### YAGPDB.xyz

**YAGPDB.xyz** bot is used for categories subscription.

For more information about how to use it, check the following tutorial:

https://docs.yagpdb.xyz/tools-and-utilities/self-assignable-roles

When you have the group and the roles configured on **YAGPDB.xyz**, the next
step is to create a custom messsage on **discord**, in the channel you want to
have this subscription mechanism.

1. In the message, add a title, a general description and the emoticons and theirs
meaning (https://unicode.org/emoji/charts/full-emoji-list.html).
2. Get the message ID (you need to activate the development mode)
3. Run the following command `!yagpdb-rolemenu create (group name) -m (message id) -nodm`,
where `(group name)` and `(message id)` are placeholders and should be replaced by
the correct values.

**Note**: An alternative to **yagpdb** would be
[**carl-bot**](https://top.gg/bot/235148962103951360). But for now, **yagpdb.xyz**
seems to be working properly for our needs.

## Development

We have an internal channel for discussions about discord: `#collab-devops-discord`.

Alos, there is a discord server for development, where we can test bots, new
configurations or new features.

If you want to join that server, you need to ask it in `#collab-devops-discord` channel.
