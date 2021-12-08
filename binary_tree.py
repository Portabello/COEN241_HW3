from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )
        # Add hosts
        host_one = self.addHost( 'h1' )
        host_two = self.addHost( 'h2' )
        host_three = self.addHost( 'h3' )
        host_four = self.addHost( 'h4' )
        host_five = self.addHost( 'h5' )
        host_six = self.addHost( 'h6' )
        host_seven = self.addHost( 'h7' )
        host_eight = self.addHost( 'h8' )

        # Add switches
        switch_one = self.addSwitch( 's1' )
        switch_two = self.addSwitch( 's2' )
        switch_three = self.addSwitch( 's3' )
        switch_four = self.addSwitch( 's4' )
        switch_five = self.addSwitch( 's5' )
        switch_six = self.addSwitch( 's6' )
        switch_seven = self.addSwitch( 's7' )

        # Add links
        self.addLink( switch_one, switch_two )
        self.addLink( switch_one, switch_five )
        self.addLink( switch_two, switch_three )
        self.addLink( switch_two, switch_four )
        self.addLink( switch_five, switch_six )
        self.addLink( switch_five, switch_seven )

        self.addLink( switch_three, host_one )
        self.addLink( switch_three, host_two )
        self.addLink( switch_four, host_three )
        self.addLink( switch_four, host_four )
        self.addLink( switch_six, host_five )
        self.addLink( switch_six, host_six )
        self.addLink( switch_seven, host_seven )
        self.addLink( switch_seven, host_eight )


topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
