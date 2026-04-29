pub struct GlobalState {
    pub nodes_online: bool,
    pub security_clearance: bool,
}

impl GlobalState {
    pub fn check_system_integrity(&self) -> bool {
        self.nodes_online && self.security_clearance
    }
}
