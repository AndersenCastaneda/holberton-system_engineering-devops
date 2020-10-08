# Fix ulimit
exec { 'Change OS Configuration':
  command => "sed -i 's/holberton/andersen/' /etc/security/limits.conf",
}
