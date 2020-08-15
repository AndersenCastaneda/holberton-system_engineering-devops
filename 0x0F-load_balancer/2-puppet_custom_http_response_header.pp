# install nginx and custom http header
exec { 'apt-get':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line {
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;'
  require => Package['nginx'],
}

service {
  ensure  => runing;
  require => Package['nginx'],
}
