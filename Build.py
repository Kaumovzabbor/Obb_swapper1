
#!/usr/bin/env python3
import os, subprocess, sys

BASE = os.path.expanduser("~/ObbSwapper")

def w(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print(f"  OK: {path}")

print("\n=== OBB SWAPPER BUILDER ===\n")

# Eski papkani o'chirish
os.system(f"rm -rf {BASE}")
os.makedirs(BASE, exist_ok=True)

w("settings.gradle", """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "ObbSwapper"
include ':app'
""")

w("build.gradle", """plugins {
    id 'com.android.application' version '8.2.2' apply false
}
""")

w("gradle.properties", """android.useAndroidX=true
android.enableJetifier=true
org.gradle.jvmargs=-Xmx1024m
""")

w("app/build.gradle", """plugins {
    id 'com.android.application'
}
android {
    namespace 'com.obbswapper'
    compileSdk 34
    defaultConfig {
        applicationId "com.obbswapper"
        minSdk 26
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }
    buildTypes {
        release { minifyEnabled false }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
}
""")

w("app/proguard-rules.pro", "")

w("app/src/main/AndroidManifest.xml", """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
        android:maxSdkVersion="29"/>
    <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
    <application
        android:allowBackup="true"
        android:label="OBB Swapper"
        android:theme="@style/Theme.ObbSwapper"
        android:requestLegacyExternalStorage="true">
        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
""")

w("app/src/main/res/values/strings.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">OBB Swapper</string>
</resources>
""")

w("app/src/main/res/values/themes.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.ObbSwapper" parent="Theme.MaterialComponents.DayNight.NoActionBar">
        <item name="colorPrimary">#58A6FF</item>
        <item name="colorPrimaryVariant">#388BFD</item>
        <item name="colorOnPrimary">#FFFFFF</item>
        <item name="android:windowBackground">#0D1117</item>
    </style>
</resources>
""")

w("app/src/main/res/drawable/input_bg.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#161B22"/>
    <corners android:radius="8dp"/>
    <stroke android:width="1dp" android:color="#21262D"/>
</shape>
""")

w("app/src/main/res/layout/activity_main.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    android:background="#0D1117">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="OBB Swapper"
        android:textSize="24sp"
        android:textStyle="bold"
        android:textColor="#58A6FF"
        android:gravity="center"
        android:paddingBottom="2dp"/>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="testobb to Android/obb"
        android:textSize="12sp"
        android:textColor="#8B949E"
        android:gravity="center"
        android:paddingBottom="16dp"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Package nomi:"
        android:textColor="#C9D1D9"
        android:textSize="13sp"
        android:paddingBottom="5dp"/>

    <EditText
        android:id="@+id/etPackageName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="com.example.mygame"
        android:textColor="#C9D1D9"
        android:textColorHint="#484F58"
        android:background="@drawable/input_bg"
        android:padding="12dp"
        android:layout_marginBottom="10dp"
        android:inputType="text"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="OBB fayl nomi (Android/obb ichida):"
        android:textColor="#C9D1D9"
        android:textSize="13sp"
        android:paddingBottom="5dp"/>

    <EditText
        android:id="@+id/etObbName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="main.12345.com.example.mygame.obb"
        android:textColor="#C9D1D9"
        android:textColorHint="#484F58"
        android:background="@drawable/input_bg"
        android:padding="12dp"
        android:layout_marginBottom="10dp"
        android:inputType="text"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Manba fayl nomi (testobb ichida):"
        android:textColor="#C9D1D9"
        android:textSize="13sp"
        android:paddingBottom="5dp"/>

    <EditText
        android:id="@+id/etSrcName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="1.obb"
        android:textColor="#C9D1D9"
        android:textColorHint="#484F58"
        android:background="@drawable/input_bg"
        android:padding="12dp"
        android:layout_marginBottom="14dp"
        android:inputType="text"/>

    <Button
        android:id="@+id/btnPermission"
        android:layout_width="match_parent"
        android:layout_height="46dp"
        android:text="Ruxsat Sorash"
        android:backgroundTint="#21262D"
        android:textColor="#8B949E"
        android:textSize="13sp"
        android:layout_marginBottom="16dp"/>

    <View android:layout_width="match_parent" android:layout_height="1dp"
        android:background="#21262D" android:layout_marginBottom="12dp"/>

    <Button
        android:id="@+id/btnDelete"
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:text="OBB ni OCHIRISH"
        android:backgroundTint="#8B0000"
        android:textColor="#FFFFFF"
        android:textStyle="bold"
        android:textSize="14sp"
        android:layout_marginBottom="12dp"/>

    <View android:layout_width="match_parent" android:layout_height="1dp"
        android:background="#21262D" android:layout_marginBottom="12dp"/>

    <Button
        android:id="@+id/btnCopyReal"
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:text="REAL faylni Kochirish"
        android:backgroundTint="#1A5C2A"
        android:textColor="#FFFFFF"
        android:textStyle="bold"
        android:textSize="14sp"
        android:layout_marginBottom="12dp"/>

    <View android:layout_width="match_parent" android:layout_height="1dp"
        android:background="#21262D" android:layout_marginBottom="12dp"/>

    <Button
        android:id="@+id/btnCopyTest"
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:text="TEST faylni Kochirish"
        android:backgroundTint="#1C3461"
        android:textColor="#FFFFFF"
        android:textStyle="bold"
        android:textSize="14sp"
        android:layout_marginBottom="12dp"/>

    <ProgressBar
        android:id="@+id/progressBar"
        style="@style/Widget.AppCompat.ProgressBar.Horizontal"
        android:layout_width="match_parent"
        android:layout_height="6dp"
        android:visibility="gone"
        android:progressTint="#58A6FF"
        android:layout_marginBottom="8dp"
        android:max="100"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Log:"
        android:textColor="#484F58"
        android:textSize="11sp"
        android:paddingBottom="4dp"/>

    <ScrollView
        android:id="@+id/scrollView"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:background="@drawable/input_bg"
        android:padding="8dp">
        <TextView
            android:id="@+id/tvLog"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="#C9D1D9"
            android:textSize="11sp"
            android:fontFamily="monospace"
            android:text="Tayyor. Malumotlarni kiriting va tugmani bosing.\\n"/>
    </ScrollView>
</LinearLayout>
""")

w("app/src/main/java/com/obbswapper/MainActivity.java", """package com.obbswapper;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.Settings;
import android.view.View;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.channels.FileChannel;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    private static final int PERMISSION_REQUEST_CODE = 100;
    private static final int MANAGE_STORAGE_REQUEST  = 101;

    private EditText etPackageName, etObbName, etSrcName;
    private ProgressBar progressBar;
    private TextView tvLog;
    private ScrollView scrollView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etPackageName = findViewById(R.id.etPackageName);
        etObbName     = findViewById(R.id.etObbName);
        etSrcName     = findViewById(R.id.etSrcName);
        progressBar   = findViewById(R.id.progressBar);
        tvLog         = findViewById(R.id.tvLog);
        scrollView    = findViewById(R.id.scrollView);

        findViewById(R.id.btnPermission).setOnClickListener(v -> requestPermission());

        findViewById(R.id.btnDelete).setOnClickListener(v -> {
            if (!checkReady()) return;
            new Thread(() -> {
                File target = new File(Environment.getExternalStorageDirectory(),
                    "Android/obb/" + etPackageName.getText().toString().trim() + "/" + getObbName());
                log("Ochirilmoqda: " + target.getAbsolutePath());
                if (!target.exists()) log("Fayl topilmadi!");
                else if (target.delete()) log("Muvaffaqiyatli ochirildi!");
                else log("Ochirib bolmadi!");
            }).start();
        });

        findViewById(R.id.btnCopyReal).setOnClickListener(v -> {
            if (!checkReady()) return;
            new Thread(() -> copyObb("testobb/real/" + getSrcName())).start();
        });

        findViewById(R.id.btnCopyTest).setOnClickListener(v -> {
            if (!checkReady()) return;
            new Thread(() -> copyObb("testobb/test/" + getSrcName())).start();
        });
    }

    private String getObbName() {
        String n = etObbName.getText().toString().trim();
        return n.isEmpty() ? "1.obb" : n;
    }

    private String getSrcName() {
        String n = etSrcName.getText().toString().trim();
        return n.isEmpty() ? "1.obb" : n;
    }

    private void copyObb(String sourcePath) {
        String pkg     = etPackageName.getText().toString().trim();
        String obbName = getObbName();
        File   ext     = Environment.getExternalStorageDirectory();
        File   source  = new File(ext, sourcePath);
        File   destDir = new File(ext, "Android/obb/" + pkg);
        File   dest    = new File(destDir, obbName);

        log("Manba  : " + source.getAbsolutePath());
        log("Maqsad : " + dest.getAbsolutePath());

        if (!source.exists()) { log("Manba fayl topilmadi!"); return; }
        log("Hajm: " + formatSize(source.length()));

        if (!destDir.exists()) {
            if (destDir.mkdirs()) log("Papka yaratildi.");
            else { log("Papka yaratib bolmadi!"); return; }
        }

        if (dest.exists()) dest.delete();

        log("Kochirish boshlandi...");
        runOnUiThread(() -> { progressBar.setProgress(0); progressBar.setVisibility(View.VISIBLE); });

        try {
            try (FileInputStream fis = new FileInputStream(source);
                 FileOutputStream fos = new FileOutputStream(dest);
                 FileChannel in = fis.getChannel();
                 FileChannel out = fos.getChannel()) {
                long total = in.size(), done = 0, chunk = 1024 * 1024L;
                while (done < total) {
                    done += in.transferTo(done, chunk, out);
                    int pct = (int)(done * 100 / total);
                    runOnUiThread(() -> progressBar.setProgress(pct));
                }
            }
            log("MUVAFFAQIYATLI! " + formatSize(dest.length()) + " kochirildi.");
        } catch (IOException e) {
            log("Xatolik: " + e.getMessage());
        } finally {
            runOnUiThread(() -> { progressBar.setProgress(0); progressBar.setVisibility(View.GONE); });
        }
    }

    private void requestPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            if (!Environment.isExternalStorageManager()) {
                startActivityForResult(new Intent(Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION,
                    Uri.parse("package:" + getPackageName())), MANAGE_STORAGE_REQUEST);
                log("Sozlamalarda Barcha fayllarni boshqarish ni YOQING!");
            } else log("Ruxsat allaqachon bor!");
        } else {
            ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.READ_EXTERNAL_STORAGE,
                             Manifest.permission.WRITE_EXTERNAL_STORAGE}, PERMISSION_REQUEST_CODE);
        }
    }

    private boolean hasPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R)
            return Environment.isExternalStorageManager();
        return ContextCompat.checkSelfPermission(this,
            Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED;
    }

    private boolean checkReady() {
        if (!hasPermission()) {
            log("Avval ruxsat bering!");
            Toast.makeText(this, "Ruxsat yoq! Birinchi tugmani bosing.", Toast.LENGTH_SHORT).show();
            return false;
        }
        if (etPackageName.getText().toString().trim().isEmpty()) {
            Toast.makeText(this, "Package nomini kiriting!", Toast.LENGTH_SHORT).show();
            return false;
        }
        return true;
    }

    private void log(String msg) {
        String t = new SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(new Date());
        runOnUiThread(() -> {
            tvLog.append("[" + t + "] " + msg + "\\n");
            scrollView.post(() -> scrollView.fullScroll(View.FOCUS_DOWN));
        });
    }

    private String formatSize(long b) {
        if (b < 1024) return b + " B";
        if (b < 1048576) return String.format(Locale.getDefault(), "%.1f KB", b / 1024.0);
        if (b < 1073741824) return String.format(Locale.getDefault(), "%.1f MB", b / 1048576.0);
        return String.format(Locale.getDefault(), "%.2f GB", b / 1073741824.0);
    }

    @Override
    public void onRequestPermissionsResult(int req, @NonNull String[] perms, @NonNull int[] res) {
        super.onRequestPermissionsResult(req, perms, res);
        if (req == PERMISSION_REQUEST_CODE)
            log(res.length > 0 && res[0] == PackageManager.PERMISSION_GRANTED
                ? "Ruxsat berildi!" : "Ruxsat rad etildi!");
    }

    @Override
    protected void onActivityResult(int req, int res, Intent data) {
        super.onActivityResult(req, res, data);
        if (req == MANAGE_STORAGE_REQUEST && Build.VERSION.SDK_INT >= Build.VERSION_CODES.R)
            log(Environment.isExternalStorageManager() ? "Ruxsat berildi!" : "Ruxsat berilmadi!");
    }
}
""")

w("gradle/wrapper/gradle-wrapper.properties", """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.6-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""")

# gradlew yuklab olish
print("\nGradle wrapper yuklanmoqda...")
os.system(f"curl -fsSL -o {BASE}/gradlew https://raw.githubusercontent.com/gradle/gradle/v8.6.0/gradlew")
os.system(f"chmod +x {BASE}/gradlew")

print("\nBuild boshlanmoqda...\n")
ret = os.system(f"cd {BASE} && ./gradlew assembleDebug --no-daemon")

if ret == 0:
    apk = None
    for root, dirs, files in os.walk(BASE):
        for f in files:
            if f.endswith(".apk"):
                apk = os.path.join(root, f)
                break
    if apk:
        os.system(f"cp {apk} ~/ObbSwapper.apk")
        print("\n=== MUVAFFAQIYATLI! ===")
        print("APK: ~/ObbSwapper.apk")
        print("Ornatish: termux-open ~/ObbSwapper.apk")
    else:
        print("APK topilmadi!")
else:
    print("Build xatosi!")
