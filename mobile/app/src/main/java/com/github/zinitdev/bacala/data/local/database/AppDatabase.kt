package com.github.zinitdev.bacala.data.local.database

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.github.zinitdev.bacala.data.local.database.dao.CategoryDao
import com.github.zinitdev.bacala.data.local.database.entity.Category

private const val DATABASE_NAME = "bacala.db"
private const val DATABASE_VERSION = 1

@Database(
    entities = [Category::class],
    version = DATABASE_VERSION
)
abstract class AppDatabase: RoomDatabase() {
    abstract fun categoryDao(): CategoryDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        operator fun invoke(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                INSTANCE ?: buildDatabase(context.applicationContext).also {
                    INSTANCE = it
                }
            }
        }

        private fun buildDatabase(context: Context): AppDatabase = Room.databaseBuilder(
            context.applicationContext,
            AppDatabase::class.java,
            DATABASE_NAME
        )
            .fallbackToDestructiveMigration(false)
            .build()
    }
}