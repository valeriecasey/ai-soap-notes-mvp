import React, { useEffect, useState } from 'react';

const NoteDisplay = () => {
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        const fetchNotes = async () => {
            try {
                const response = await fetch('/api/notes'); // Adjust the endpoint as necessary
                const data = await response.json();
                setNotes(data);
            } catch (error) {
                console.error('Error fetching notes:', error);
            }
        };

        fetchNotes();
    }, []);

    return (
        <div className="note-display">
            <h2>SOAP Notes</h2>
            {notes.length > 0 ? (
                notes.map((note, index) => (
                    <div key={index} className="note">
                        <h3>Subjective</h3>
                        <p>{note.subjective}</p>
                        <h3>Objective</h3>
                        <p>{note.objective}</p>
                        <h3>Assessment</h3>
                        <p>{note.assessment}</p>
                        <h3>Plan</h3>
                        <p>{note.plan}</p>
                    </div>
                ))
            ) : (
                <p>No notes available.</p>
            )}
        </div>
    );
};

export default NoteDisplay;