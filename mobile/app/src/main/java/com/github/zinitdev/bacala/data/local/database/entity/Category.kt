package com.github.zinitdev.bacala.data.local.database.entity

import androidx.room.Embedded
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "category")
data class Category(
    @PrimaryKey(autoGenerate = true)
    val id: Long? = null,
    @Embedded
    val base: BaseEntity,
    val name: String
)
