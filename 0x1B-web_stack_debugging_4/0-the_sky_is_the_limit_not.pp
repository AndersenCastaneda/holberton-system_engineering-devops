# Fix ulimit
exec { 'Fix ulimit':
  onlyif  => 'test -e /etc/default/nginx',
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

exec { 'Restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
