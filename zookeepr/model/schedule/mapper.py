from sqlalchemy.orm import mapper, relation
from sqlalchemy.sql import select

from tables import stream
from domain import Stream, Talk
from zookeepr.model.proposal.tables import proposal, person_proposal_map
from zookeepr.model.proposal.domain import ProposalType
from zookeepr.model.core.domain import Person

# map Talk onto accepted proposals.

mapper(Talk, select([proposal],
                    proposal.c.accepted==True
                    ).alias('proposal_talks'),
       properties = {
    'type': relation(ProposalType),
    'people': relation(Person, secondary=person_proposal_map,
                       backref='accepted_talks'),
    }
       )
