#String Section Rostering Utility
## Software Development Plan

### Purpose

The utility of this application is two-fold. It is designed to:

1. Maintain a pseudo-database of musicians, including what instrument they play, and the specific roles that they perform. The program allows for basic CRUD operations to be performed on these musicians.

2. Design rosters for specific concert programs, allowing both for manual and automatic filling of positions, whilst ensuring that players aren't put into inappropriate positions.

### String Rostering 101

For those not familiar with how classical string sections work, here is a quick rundown. There are four string instruments requiring rostering in an orchestra; violins, violas, cellos and double basses. For each of these instruments, there will be one physical part in the music to play, meaning that all players of the same instrument will play the same music. The exception to this is the violin, for which there are two parts. These sections are known as the first and second violins respectively.

Therefore there are five sections in a string section:
* First violins
* Second violins
* Violas
* Cellos
* Double Bass

There are also rules governed by the positions within each section that a musician will sit. There are two categories of players; principal and tutti musicians. Principals will always sit in the first chair of their respective sections, whereas tutti players will sit anywhere else.

Violin roles are a little different:
* 1st Violin, 1st chair is known as the __Concert Master__
* 1st Violin, 2nd chair is known as the __Associate Concert Master__
* 1st Violin, 3rd chair is the __Principal__
* 2nd Violin, 1st chair is the __Principal 2nd Violin__

There are two types of employment in the profession as well; regular and casual musicians. Regular musicians are kept on salary whilst casual musicians are brought in for specific programs. 


### The Rules of the Game

A musician should always sit in their designated position, however a secondary position can also be assigned to that player. Ultimately however, the program will allow any musician to sit in any chair provided that they play the appropriate instrument. A musician can only be associated with a single string instrument, the norm in the classical music profession.

### Who is this Program for?

This app is appropriate for both orchestral administrators who need to 