---
title: "Guard the Dopamine Factory: A Five-Minute Game That Makes Students Recall Where Each Drug Strikes"
date: 2026-10-28T23:30:00-04:00
area: Science education, game-based learning
summary: A lane-defense game for first-year biology. Drugs walk in as zombies, and students stop each one by placing the part of the dopamine machine it damages. About 40 recalls in five minutes, with feedback after every mistake and danger levels drawn from overdose data.
image: media/projects/guard-the-factory/game-overview.webp
tags:
- Science Education
- Game-Based Learning
- AI in Education
- Neuroscience
---

[Guard the Dopamine Factory](https://addictions.win/Guard_the_Factory.html) is a five-minute game I designed for the addiction lesson in first-year biology, played right after Mouse Party and [The Dopamine Machine](/project/dopamine-machine/). It has one goal: students should remember which part of the dopamine machine each drug damages. Recalling a fact makes it stick better than watching it again, so the game never shows the answer first. Each drug walks in as a zombie with its name over its head, and the student has to recall its part and act on it, about 40 times in five minutes.

## How it plays

![The game in play: the factory with four parts on the left, guards labeled Dopamine neuron, GABA, DAT and Vesicles on the lawn, and drug zombies walking in from the bloodstream](media/projects/guard-the-factory/game-overview.webp)

*The factory holds the four parts of the dopamine machine. Each guard is one of those parts, and its shots hurt only the drugs that damage it.*

- **The factory** shows the four parts these drugs act on: the dopamine neuron, the GABA brake, the vesicles and the recycle pumps (DAT). They are drawn with the lesson's own drawing code, so students see exactly the pictures they just studied.
- **Each drug** carries one bomb for every part it damages. Meth and alcohol carry two, so they need two kinds of guard.
- **A wrong guard does nothing.** A drug that reaches the factory bombs its parts, and the score drops.
- **Guards last 30 seconds and cost ATP,** so students cannot cover every lane in advance; they have to read each name.
- **Drugs arrive one kind at a time,** in the order of the lesson, then all together near the end.

## Feedback at the moment of the mistake

![A GABA guard's shots pass through cocaine, a heroin bomb hits the brake operator, a stopped nicotine zombie turns to smoke, and the Field notes explain each event](media/projects/guard-the-factory/game-feedback.webp)

*The GABA guard does nothing to cocaine, and Field notes says why: cocaine damages the recycle pumps.*

Every mistake explains itself in one sentence, such as "The GABA guard has no effect on Cocaine. Cocaine damages the recycle pumps." When a bomb lands, the message uses Mouse Party's own words. Each new drug has a Hint button, and the end screen lists every drug with its part as a review sheet.

![The end screen: the score, the parts that were bombed, and a table of every drug with the part it damages](media/projects/guard-the-factory/game-end.webp)

## Danger that follows real data

The numbers carry meaning. A drug that kills more easily in one dose takes more hits and costs more points, and a more common drug shows up more often.

| Drug | Hits to stop | Points lost per bomb | How often | Why |
|---|---|---|---|---|
| Fentanyl | 10 | −300 | rare | Involved in about 74,000 of 108,000 U.S. overdose deaths in 2022 |
| Heroin, meth, cocaine | 4 to 6 | −200 | rare to medium | The next highest overdose risks |
| Alcohol | 4 per bomb | −100 | most common | Kills mostly over years |
| Marijuana | 2 | −50 | most common | Fatal overdose is very rare |
| Nicotine | 1, in threes | −50 | common | About 1 in 3 users become dependent |

Fentanyl is the zombie that will not go down; marijuana is easy to stop but keeps coming. The teacher notes add a caution: easy to stop is not harmless, since about 1 in 10 people who use marijuana develop a use disorder.

![The start screen with the goal and a checklist of drugs, with alcohol, cocaine and the three opioids ticked by default](media/projects/guard-the-factory/game-start.webp)

*Teachers pick the drugs for each class. One HTML file runs in any browser, with no install.*

## Compared with other addiction games

| Game | What students do | What they must recall |
|---|---|---|
| [Mouse Party](https://learn.genetics.utah.edu/content/addiction/mouse/) | Watch narrated slides for seven drugs | Nothing during the activity |
| [Meth Mouse](https://learn.genetics.utah.edu/content/addiction/methmouse/) | Run one synapse with methamphetamine | Nothing; one drug |
| NIDA's [Pick a Card](https://cdgr.ucsb.edu/node/382) | Answer quiz questions | One fact at a time, outside any model |
| [You VS Drugs](https://papers.academic-conferences.org/index.php/ecgbl/article/view/1417) | Travel through a 3D synapse | Neurotransmitter function |
| [Immune Defense](https://www.molecularjig.com/immune-defense-game/immune-defense-2/) | Tower defense with immune cells | The same genre, in immunology |

Mouse Party is still the best short explanation, and my lesson plays it first. This game adds what comes next: recall as the core move, with drugs mixed after each is introduced; the same pictures as the lesson; numbers grounded in data; and a balance tested before class.

## Teaching with AI

The game went from idea to classroom in one day. I made the teaching decisions: the goal, the metaphors, what to leave out, and what every number means. AI made each step faster and checkable:

- **Checking sources.** With an AI agent I extracted the text of Mouse Party and Meth Mouse from their game files and compared every drug with our machine. We found two claims in Meth Mouse that go beyond current evidence, and the lesson now flags them.
- **Grounding numbers in data.** AI searches found the CDC overdose figures and dependence estimates behind each drug's settings.
- **Building through specification.** An AI coding agent turned my plain-language rules into code, art and sound, so I published seven versions in one day, each answering a problem found in testing.
- **Testing with simulated players.** Scripted agents played full games after every change. A player who read the drug names scored about +3,850; one who filled every lane with all four guards scored about −6,050.

## Design thinking

- **Start from the learning goal.** My first draft had students place antidotes. That trained the wrong memory, so each guard became a part of the machine.
- **Borrow the familiar, draw our own.** A lane-defense layout needs no instructions; the pictures come from the lesson.
- **Only parts in our machine.** Ecstasy and LSD act mainly on serotonin, so I left them out rather than invent a part.
- **Make mistakes informative.** Immediate, specific feedback and retrieval practice are two of the strongest levers on learning ([Hattie & Timperley, 2007](https://doi.org/10.3102/003465430298487); [Roediger & Karpicke, 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)).
- **One drug at a time, then mixed,** so beginners learn one part at a time and then practice telling drugs apart ([Rohrer & Taylor, 2007](https://doi.org/10.1007/s11251-007-9015-8)).
- **Close the loopholes.** Permanent guards let players fill every lane and stop thinking; 30-second guards fixed it.
- **Design for the real room.** First-year words, sound tuned for laptop speakers, and a game that ends on a review sheet.

The game is a teaching model: drugs do not carry bombs, and "bombs the brake operator" means "acts on the GABA neuron".

**Links:** [Play the game](https://addictions.win/Guard_the_Factory.html) · [The Dopamine Machine](/project/dopamine-machine/) · [All lessons](https://addictions.win/lessons.html) · [Source on GitHub](https://github.com/gladcolor/addiction-3d-lessons)
