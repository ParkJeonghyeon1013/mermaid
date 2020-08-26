from s1_seaweed import s1_intro, s1_game, s1_outro
from s2_pearl import s2_game2, s2_game1, s2_intro, s2_outro
from s3_crab import money, potion_effect
from c1_character import mermaid

print("스테이지1")
s1_intro()
s1_game()
s1_outro()

print("\n스테이지2")
s2_intro()
num = s2_game1()
s2_game2(num)
s2_outro()

print("\n마지막 소라게")
money()
potion_effect()