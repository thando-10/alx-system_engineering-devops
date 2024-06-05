#Fixes  bad "phpp" extensions to "php" in "wp-settings.php".

exec{'fix-workpress':
 command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
 path => '/usr/local/bin/ and /bin'
}
