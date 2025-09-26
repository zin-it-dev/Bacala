package com.github.zinitdev.bacala.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.github.zinitdev.bacala.ui.screens.HomeScreen
import com.github.zinitdev.bacala.ui.screens.LoginScreen

@Composable
fun AppNavHost(navController: NavHostController, startDestination: String = Screen.Home.route) {
    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        composable(Screen.Home.route) {
            HomeScreen(
                onNavigate = {
                    navController.navigate(Screen.Login.route)
                }
            )
        }
        composable(Screen.Login.route) {
            LoginScreen(
                onNavigate = {
                    navController.navigate(Screen.Home.route)
                }
            )
        }
    }
}