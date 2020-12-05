package com.example.guardcar;
import androidx.appcompat.app.AppCompatActivity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.view.KeyEvent;
import android.view.View;
import android.webkit.GeolocationPermissions;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        final WebView webview = new WebView(this);
        String site = "https://guardcar.herokuapp.com/";
        webview.loadUrl(site);
        setContentView(webview);
        webview.getSettings().setJavaScriptEnabled(true);
        webview.setWebViewClient(new WebViewClient(){
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String site) {
                view.loadUrl(site);
                return false;
            }
        });
        AlertDialog.Builder dialog = new AlertDialog.Builder(this);
        webview.setWebChromeClient(new WebChromeClient(){

            @Override
            public void onGeolocationPermissionsShowPrompt(final String origin,
                                                           final GeolocationPermissions.Callback callback) {
                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                builder.setTitle("Localização");
                builder.setMessage( " Ative sua Localizaçao").setCancelable(true).setPositiveButton("ativar",
                        new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog,
                                                int id) {
                                // origin, allow, remember
                                Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS); startActivityForResult(intent, 1);
                            }
                        })
                        .setNegativeButton("não ativar",
                                new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog,
                                                        int id) {
                                        // origin, allow, remember
                                    }
                                });AlertDialog alert = builder.create();
                                alert.show();

                webview.setOnKeyListener(new View.OnKeyListener()
                {@Override
                    public boolean onKey(View v, int keyCode, KeyEvent event)
                    { if(event.getAction() == KeyEvent.ACTION_DOWN)
                        { WebView webView = (WebView) v;
                            switch(keyCode)
                            { case KeyEvent.KEYCODE_BACK:
                                    if(webView.canGoBack())
                                    {
                                        webView.goBack();
                                        return true;
                                    }break;
                            }
                        }return false;
                    }
                });
            }

        });
    }
}