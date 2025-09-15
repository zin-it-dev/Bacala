package com.github.zinitdev.bacala.data.local.database.entity

import androidx.room.ColumnInfo
import androidx.room.Embedded
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey

@Entity(
    tableName = "book",
    foreignKeys = [ForeignKey(
        entity = Category::class,
        parentColumns = ["id"],
        childColumns = ["category_id"],
        onDelete = ForeignKey.CASCADE)
    ],
    indices = [Index("category_id")]
)
data class Book(
    @PrimaryKey(autoGenerate = true)
    val id: Long? = null,
    @Embedded
    val base: BaseEntity,
    val title: String,
    val price: Float = 0.00F,
    @ColumnInfo(name = "category_id")
    val categoryId: Long
)
