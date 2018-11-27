package rhjunction.candyapp.core

import android.arch.persistence.room.Room
import android.arch.persistence.room.RoomDatabase
import android.content.Context

abstract class AppDb : RoomDatabase() {
//    abstract fun playlistDao() : PlaylistDAO
//    abstract fun watchedDao() : WatchedDAO
    abstract fun dao(): DAO

    companion object Factory {
        private var instance: AppDb? = null
        fun getInstance(context: Context) : AppDb {
            if (instance == null) {
                instance = Room.databaseBuilder(context,
                    AppDb::class.java,
                    "app-db")
                    .build()
            }
            return instance!!
        }
    }
}