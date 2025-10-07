package com.github.zinitdev.bacala.navigation

sealed class Screen(val route: String) {
    object Home : Screen("home")
    object AuthGraph : Screen("auth_graph")
    object Login : Screen("login")
}