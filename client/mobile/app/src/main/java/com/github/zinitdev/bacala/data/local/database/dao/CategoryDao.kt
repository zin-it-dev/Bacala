package com.github.zinitdev.bacala.data.local.database.dao

import androidx.room.Dao
import androidx.room.Query
import com.github.zinitdev.bacala.data.local.database.entity.Category

@Dao
interface CategoryDao {
    @Query("SELECT * FROM category WHERE is_active = 1")
    suspend fun getCategories(): List<Category>
}