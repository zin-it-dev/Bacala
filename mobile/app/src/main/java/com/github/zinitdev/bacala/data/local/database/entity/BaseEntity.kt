package com.github.zinitdev.bacala.data.local.database.entity

data class BaseEntity (
    val isActive: Boolean = true,
    val dateCreated: Long = System.currentTimeMillis(),
    val dateUpdated: Long = System.currentTimeMillis()
)