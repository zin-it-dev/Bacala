package com.github.zinitdev.bacala.ui.screens

import android.app.Activity
import android.widget.Toast
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.firebase.ui.auth.FirebaseAuthUIActivityResultContract
import com.google.firebase.auth.FirebaseAuth
import com.firebase.ui.auth.AuthUI


@Composable
fun LoginScreen(onAuthSuccess: () -> Unit) {
    val context = LocalContext.current
    val auth = FirebaseAuth.getInstance()

    val signInLauncher = rememberLauncherForActivityResult(
        FirebaseAuthUIActivityResultContract(),
    ) { res ->
        if (res.resultCode == Activity.RESULT_OK) {
            val user = auth.currentUser
            // Nếu bạn muốn gửi token lên Flask, hãy làm ở đây:
            // user?.getIdToken(true)?.addOnSuccessListener { tokenResult -> ... }
            onAuthSuccess()
        } else {
            val response = res.idpResponse
            if (response != null) {
                Toast.makeText(context, "Error: ${response.error?.message}", Toast.LENGTH_LONG).show()
            }
        }
    }

    val providers = arrayListOf(
        AuthUI.IdpConfig.GoogleBuilder().build(),
        AuthUI.IdpConfig.EmailBuilder().build()
    )

    Column(
        modifier = Modifier
            .padding(48.dp)
            .fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        Text(text = "Log In")
        Spacer(modifier = Modifier.height(32.dp))

        Button(onClick = {
            val signInIntent = AuthUI.getInstance()
                .createSignInIntentBuilder()
                .setAvailableProviders(providers)
                .build()
            signInLauncher.launch(signInIntent)
        }) {
            Text(text = "Log In")
        }
    }
}