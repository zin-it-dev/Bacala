package com.github.zinitdev.bacala

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.navigation.compose.rememberNavController
import com.github.zinitdev.bacala.navigation.AppNavHost
import com.github.zinitdev.bacala.ui.theme.BacalaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            BacalaTheme {
                val navController = rememberNavController()
                AppNavHost(navController = navController)
            }
        }
    }
}

