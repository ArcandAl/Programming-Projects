package com.example.myfirstapp;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import org.w3c.dom.Text;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    TextView display;
    long startTime;
    EditText et;
    String information;
    Hashtable<String, Long> dict = new Hashtable<String, Long>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        display = (TextView) findViewById(R.id.TimerView);
        display.setTextColor(Color.WHITE);
        display.setText("Bounty Information and Timer will be here");
        et = (EditText) findViewById(R.id.EnterInfo);
        et.setTextColor(Color.WHITE);

    }

    /** Called when start button is pressed*/
    public void startTimer(View view) {
        startTime = System.currentTimeMillis();
        information = et.getText().toString();
        dict.put(information, startTime);
    }

    /** Called when display button is pressed */
    public void displayInfo(View view) {
        long elapsedTime = System.currentTimeMillis() - dict.get(information);
        long elapsedSeocnds = elapsedTime / 1000;
        long secondsDisplay = elapsedSeocnds % 60;
        long elapsedMinutes = elapsedSeocnds / 60;
        display.setText(information + ": " + String.valueOf(elapsedMinutes) + " Min "+ String.valueOf(secondsDisplay) + " Sec");
    }
}
