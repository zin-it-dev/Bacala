package com.github.zinitdev.bacala.ui.screens

import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import com.github.zinitdev.bacala.ui.components.Greeting
import androidx.compose.foundation.layout.Column
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.ui.Alignment
import com.google.firebase.auth.FirebaseAuth

@Composable
fun HomeScreen(onNavigate: () -> Unit, onLogOut: () -> Unit) {
    val auth = FirebaseAuth.getInstance()

    Column(
        modifier = Modifier
            .padding(48.dp)
            .fillMaxSize(),
        verticalArrangement = Arrangement.spacedBy(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Greeting(name = "${auth.currentUser?.email}")
        Spacer(modifier = Modifier.height(32.dp))

        Button(onClick = { onNavigate() }) {
            Text(text = "Go to")
        }
        Button(onClick = {
            auth.signOut()
            onLogOut()
        }) {
            Text(text = "Log Out")
        }
    }
}

@Preview(showBackground = true)
@Composable
fun HomeScreenPreview() {
    HomeScreen(onNavigate = {}, onLogOut = {})
}