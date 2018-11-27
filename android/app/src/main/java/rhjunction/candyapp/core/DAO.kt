package rhjunction.candyapp.core

import android.arch.persistence.room.*

@Dao
interface DAO {

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    fun insertScore(userScore: UserScore)

    @Update(onConflict = OnConflictStrategy.IGNORE)
    fun updateScore(userScore: UserScore)

    @Transaction
    fun upsert(userScore: UserScore) {
        insertScore(userScore)
        updateScore(userScore)
    }
}