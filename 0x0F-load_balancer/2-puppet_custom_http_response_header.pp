# install nginx and custom http header
exec { 'apt-get':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default'
  after   => 'server_name _;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_line { 'not_found':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default'
  after   => 'server_name _;',
  line    => 'error_page 404 /custom_404.html;',
  require => Package['nginx'],
}

file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;'
  require => Package['nginx'],
}

file { 'index':
  content => 'Holberton School',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => runing;
  require => Package['nginx'],
}
