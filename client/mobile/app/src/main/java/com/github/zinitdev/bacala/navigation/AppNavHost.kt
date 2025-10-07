package com.github.zinitdev.bacala.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.navigation
import com.github.zinitdev.bacala.ui.screens.HomeScreen
import com.github.zinitdev.bacala.ui.screens.LoginScreen

@Composable
fun AppNavHost(navController: NavHostController, startDestination: String) {
    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        composable(Screen.Home.route) {
            HomeScreen(
                onLogOut = {
                    navController.navigate(Screen.AuthGraph.route) {
                        popUpTo(Screen.Home.route) { inclusive = true }
                    }
                },
                onNavigate = {
                    navController.navigate(Screen.Login.route)
                }
            )
        }

        navigation(
            startDestination = Screen.Login.route,
            route = Screen.AuthGraph.route
        ) {
            composable(Screen.Login.route) {
                LoginScreen(
                    onAuthSuccess = {
                        navController.navigate(Screen.Home.route) {
                            popUpTo(Screen.AuthGraph.route) {
                                inclusive = true
                            }
                        }
                    }
                )
            }
        }
    }
}