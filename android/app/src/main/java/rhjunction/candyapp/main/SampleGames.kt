package rhjunction.candyapp.main

data class Game(val name: String,
                val imageResName: String)

val defaultImageName = "angry_birds"

val sampleGames = mutableListOf(Game("JellyBlast", "jelly_blast"),
                                Game("Angry Birds", "angry_birds"),
                                Game("Alepa game", "alepa_game"))