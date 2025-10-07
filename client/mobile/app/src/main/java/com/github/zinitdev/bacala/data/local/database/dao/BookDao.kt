package com.github.zinitdev.bacala.data.local.database.dao

import androidx.room.Dao
import androidx.room.Query
import com.github.zinitdev.bacala.data.local.database.entity.Book

@Dao
interface BookDao {
    @Query("SELECT * FROM book WHERE is_active = 1")
    suspend fun getBooks(): List<Book>
}