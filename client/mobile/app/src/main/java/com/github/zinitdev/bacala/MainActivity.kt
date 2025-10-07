package com.github.zinitdev.bacala

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.navigation.compose.rememberNavController
import com.github.zinitdev.bacala.navigation.AppNavHost
import com.github.zinitdev.bacala.navigation.Screen
import com.github.zinitdev.bacala.ui.theme.BacalaTheme
import com.google.firebase.auth.FirebaseAuth

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val firebaseAuth = FirebaseAuth.getInstance()
        val startDestination = if (firebaseAuth.currentUser != null) {
            Screen.Home.route
        } else {
            Screen.AuthGraph.route
        }

        enableEdgeToEdge()
        setContent {
            BacalaTheme {
                val navController = rememberNavController()
                AppNavHost(navController = navController, startDestination = startDestination )
            }
        }
    }
}

