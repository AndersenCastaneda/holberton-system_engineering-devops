exec { 'Fix 500 error':
	onlyif  => 'test -e /var/www/html/wp-settings.php',
	command => 'sed -i "s/phpp/php" /var/www/html/wp-settings.php',
}
