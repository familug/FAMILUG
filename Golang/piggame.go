package main

import (
	"log"
	"math/rand"
	"time"
)

const (
	scoreToWinAGame = 100
)

type Player struct {
	Name string
}

func (p *Player) roll() int {
	return rand.Intn(6) + 1
}

func (p *Player) hold(score int) bool {
	return score > 10
}

func (p *Player) play(userScore, turnTotal int) int {
	turnScore := p.roll()
	log.Printf("%s rolls: %d\n", p.Name, turnScore)
	if turnScore == 1 {
		return userScore
	} else {
		turnTotal += turnScore
		if p.hold(turnTotal) {
			log.Printf("%s holds", p.Name)
			return userScore + turnTotal
		} else {
			return p.play(userScore, turnTotal)
		}
	}
}

func playGame(p1, p2 Player) (winner Player, turns int) {
	p1Score, p2Score := 0, 0
	for i := 0; ; i++ {
		p1Score = p1.play(p1Score, 1)
		p2Score = p2.play(p2Score, 1)
		log.Printf("Foo: %d - Bar: %d", p1Score, p2Score)
		if p1Score >= scoreToWinAGame {
			return p1, i
		}
		if p2Score >= scoreToWinAGame {
			return p2, i
		}
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	p1 := Player{"Foo"}
	p2 := Player{"Bar"}
	winner, turns := playGame(p1, p2)
	log.Printf("%s won after %d turns.", winner.Name, turns)
	p1Wins := 0
	nogame := 100
	for i := 0; i < nogame; i++ {
		winner, _ := playGame(p1, p2)
		if winner == p1 {
			p1Wins += 1
		}
	}
	log.Printf("%s won %d, %s won %d", p1.Name, p1Wins, p2.Name, nogame-p1Wins)
}
