package com.github.zinitdev.bacala.data.local.database.entity

import androidx.room.ColumnInfo

data class BaseEntity (
    @ColumnInfo("is_active")
    val isActive: Boolean = true,
    @ColumnInfo("date_created")
    val dateCreated: Long = System.currentTimeMillis(),
    @ColumnInfo("date_updated")
    val dateUpdated: Long = System.currentTimeMillis()
)