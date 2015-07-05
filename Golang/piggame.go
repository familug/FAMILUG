package main

import (
	"log"
	"math/rand"
	"time"
)

const (
	score_to_win_a_game = 100
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

func (p *Player) play(user_score, turn_total int) int {
	turn_score := p.roll()
	log.Printf("%s rolls: %d\n", p.Name, turn_score)
	if turn_score == 1 {
		return user_score
	} else {
		turn_total += turn_score
		if p.hold(turn_total) {
			log.Printf("%s holds", p.Name)
			return user_score + turn_total
		} else {
			return p.play(user_score, turn_total)
		}
	}
}

func play_a_game(p1, p2 Player) (winner Player, turns int) {
	p1_score, p2_score := 0, 0
	for i := 0; ; i++ {
		p1_score = p1.play(p1_score, 1)
		p2_score = p2.play(p2_score, 1)
		log.Printf("Foo: %d - Bar: %d", p1_score, p2_score)
		if p1_score >= score_to_win_a_game {
			return p1, i
		}
		if p2_score >= score_to_win_a_game {
			return p2, i
		}
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	p1 := Player{"Foo"}
	p2 := Player{"Bar"}
	winner, turns := play_a_game(p1, p2)
	log.Printf("%s won after %d turns.", winner.Name, turns)
	p1_wins := 0
	nogame := 100
	for i := 0; i < nogame; i++ {
		winner, _ := play_a_game(p1, p2)
		if winner == p1 {
			p1_wins += 1
		}
	}
	log.Printf("%s won %d, %s won %d", p1.Name, p1_wins, p2.Name, nogame-p1_wins)
}
