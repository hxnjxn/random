function normalizeServices() {
	  var projectId = Session.get('projectId')
		    var ports = Services.find({
			        'projectId': projectId
			      })

	    var serverMap = {
		        22: 'SSH',
			    21: 'FTP',
			        23: 'TELNET',
				    25: 'SMTP',
				        53: 'DNS',
					    79: 'FINGER',
					        80: 'HTTP',
						    81: 'HTTP',
						        111: 'RPC',
							    123: 'NTP',
							        135: 'MS-RPC',
								    137: 'NETBIOS',
								        139: 'CIFS',
									    161: 'SNMP',
									        443: 'HTTPS',
										    445: 'CIFS',
										        500: 'ISAKMP',
											    1433: 'MS-SQL-TDS',
											        1434: 'MS-SQL-MONITOR',
												    2222: 'SSH',
												        2638: 'SYBASE',
													    3389: 'MS RDP',
													        4786: 'SMARTINSTALL',
														    5060: 'SIP',
														        5222: 'XMPPCLIENT',
															    7777: 'HTTP',
															        8000: 'HTTP',
																    8080: 'HTTP',
																        8081: 'HTTP',
																	    8443: 'HTTPS',
																	        9090: 'HTTP',
																		    49316: 'MS-SQL-TDS'
																			      }

	      ports.forEach(function (port) {
		          var service = port.service.toUpperCase()
		          var mappedService = serverMap[port.port]
		          if (mappedService) {
				        service = mappedService
		          }

	          if (service === '') {
			        service = 'UNKNOWN'
		          }

		      service = service.replace('WWW', 'HTTP')
		          service = service.replace('HTTP-ALT', 'HTTP')
		          service = service.replace('HTTPS-ALT', 'HTTPS')
		          service = service.replace(/\?/g, '')

		          if (service === port.service) {
				        return
		          }

	          Meteor.call('setServiceService', projectId, port._id, service, function (err) {
			        if (!err) {
					        console.log('Modified service')
			        } else {
					        console.log(err)
			        }
				    })
		    })
}

