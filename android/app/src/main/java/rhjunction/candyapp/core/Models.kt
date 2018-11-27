package rhjunction.candyapp.core

import android.arch.persistence.room.Entity
import android.arch.persistence.room.PrimaryKey

@Entity(tableName = "user_scores")
data class UserScore(@PrimaryKey val username: String, val score: Int)