package com.github.zinitdev.bacala.data.local.database.dao

import androidx.room.Dao
import androidx.room.Query
import com.github.zinitdev.bacala.data.local.database.entity.Category
import kotlinx.coroutines.flow.Flow

@Dao
interface CategoryDao {
    @Query("SELECT * FROM category WHERE is_active = 1")
    fun getCategories(): Flow<List<Category>>
}