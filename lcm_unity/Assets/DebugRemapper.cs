using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class DebugRemapper : MonoBehaviour {

	List<string> buffer = new List<string> ();
	int counter = 0;

	void Start () {
		Application.RegisterLogCallback (HandleLog);
	}

	void HandleLog(string a, string b, LogType t){
		buffer.Add (a);
		if (buffer.Count > 25)
			buffer.RemoveAt (0);
	}

	void OnGUI(){
		for (int i = 0; i < buffer.Count; i++) {
			GUILayout.Label(buffer[i]);
		}
	}
}
