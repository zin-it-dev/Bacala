import { initializeApp } from "firebase/app";
import { useFirebaseAuth } from "vuefire";

var firebaseConfig = {
  apiKey: "YourConfigHere",
  authDomain: "YourConfigHere",
  projectId: "YourConfigHere",
  storageBucket: "YourConfigHere",
  messagingSenderId: "YourConfigHere",
  appId: "YourConfigHere",
};

export const firebaseApp = initializeApp(firebaseConfig);
export const auth = useFirebaseAuth();
