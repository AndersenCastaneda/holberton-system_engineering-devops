# Fix ulimit
exec { 'Change OS Configuration':
  command => "sed -i 's/holberton/andersen/' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
