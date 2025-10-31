package com.github.zinitdev.bacala.data.local.database.dao

import androidx.room.Dao
import androidx.room.Query
import com.github.zinitdev.bacala.data.local.database.entity.Book
import kotlinx.coroutines.flow.Flow

@Dao
interface BookDao {
    @Query("SELECT * FROM book WHERE is_active = 1")
    fun getBooks(): Flow<List<Book>>
}